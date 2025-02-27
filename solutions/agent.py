from llm import llm
from graph import graph
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.tools import Tool
from langchain_neo4j import Neo4jChatMessageHistory
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain import hub
from utils import get_session_id

from tools.vector import get_movie_plot
from tools.cypher import cypher_qa

import time
from openai import APIError

import json

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie expert providing information about movies."),
        ("human", "{input}"),
    ]
)

movie_chat = chat_prompt | llm | StrOutputParser()

def safe_tool_call(func, *args, **kwargs):
    """
    Executes a tool safely and ensures it returns a well-formatted JSON response.
    """
    try:
        result = func(*args, **kwargs)
        if isinstance(result, str):  # Vérifier si la réponse est une chaîne de texte brute
            result = json.loads(result)  # Essayer de la convertir en JSON
        return result
    except (json.JSONDecodeError, TypeError) as e:
        print(f"⚠️ Tool Error: Output was not valid JSON. Error: {str(e)}")
        return {"error": "Invalid response format"}

tools = [
    Tool.from_function(
        name="General Chat",
        description="For general movie chat not covered by other tools",
        func=movie_chat.invoke,
    ), 
    Tool.from_function(
        name="Movie Plot Search",  
        description="For when you need to find information about movies based on a plot",
        func=lambda *args, **kwargs: safe_tool_call(get_movie_plot, *args, **kwargs),
    ),
    Tool.from_function(
        name="Movie information",
        description="Provide information about movies questions using Cypher",
        func=lambda *args, **kwargs: safe_tool_call(cypher_qa, *args, **kwargs),
    )
]

def get_memory(session_id):
    return Neo4jChatMessageHistory(session_id=session_id, graph=graph)

agent_prompt = PromptTemplate.from_template("""
You are a movie expert providing information about movies.
Be as helpful as possible and return as much information as possible.
Do not answer any questions that do not relate to movies, actors or directors.

Do not answer any questions using your pre-trained knowledge, only use the information provided in the context.

Important: Always follow the exact output format below.
If you deviate, the system will not understand your response.

If you cannot find an answer using the tools, respond with:
Final Answer: I'm sorry, but I couldn't find any information about that in my database.

TOOLS:
------

You have access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3,
)

chat_agent = RunnableWithMessageHistory(
    agent_executor,
    get_memory,
    input_messages_key="input",
    history_messages_key="chat_history",
)

def generate_response(user_input):
    """
    Calls the Conversational agent and handles errors.
    """
    max_retries = 3  # Nombre de tentatives max
    for attempt in range(max_retries):
        try:
            response = chat_agent.invoke(
                {"input": user_input},
                {"configurable": {"session_id": get_session_id()}},
            )
            return response['output']
        except APIError as e:
            print(f"⚠️ OpenAI API Error: {str(e)} - Attempt {attempt+1}/{max_retries}")
            time.sleep(2)  # Attendre avant de réessayer
    return "Sorry, I encountered an issue while generating a response."
