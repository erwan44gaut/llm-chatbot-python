# 🎬 Neo4j Movie Query Testing Guide

## 🟢 Basic Movie Retrieval (Direct Query)
- **Which movies were directed by Christopher Nolan?**  
  ➝ *Expected:* Neo4j should return a list of movies directed by Nolan.

- **What is the plot of "Inception"?**  
  ➝ *Expected:* The bot should fetch the plot summary from Neo4j.

## 🟡 Complex Search (Multiple Conditions & Relationships)
- **Find all horror movies released after 2010 with an IMDb rating above 7.5.**  
  ➝ *Expected:* The bot should filter horror movies based on both year and rating.

- **Which actors have worked in both action and sci-fi movies?**  
  ➝ *Expected:* The bot should analyze the relationships between actors and movie genres.

## 🟠 Reasoning Over Relationships & Contextual Understanding
- **List all directors who have collaborated with Leonardo DiCaprio more than once.**  
  ➝ *Expected:* Neo4j should count relationships between DiCaprio and directors.

- **Which movies feature both Tom Hardy and Cillian Murphy?**  
  ➝ *Expected:* The bot should cross-check actors in shared movies.

## 🔴 Handling Missing Information & Intelligent Fallback
- **What is the budget of "Interstellar"?**  
  ➝ *Expected:* If budget data exists in Neo4j, return it. Otherwise, see if ChatGPT can provide a general estimate.

- **Recommend some highly rated movies similar to "Blade Runner 2049".**  
  ➝ *Expected:* The bot should ideally find movies with a similar genre & style in Neo4j.

## 🔵 User Context Awareness & Multi-Turn Memory
- **(First question) Show me all movies featuring Robert Downey Jr.**  
- **(Follow-up question) Which of these were directed by Jon Favreau?**  
  ➝ *Expected:* The bot should remember the previous list and filter accordingly.

## 🟣 Error Handling & Edge Cases
- **Give me a list of movies directed by an AI.**  
  ➝ *Expected:* If no data exists in Neo4j, the bot should gracefully handle the query instead of breaking.

---

## 🟢 Recherche approfondie sur les films
- **Which movies were released in the same year as "The Matrix"?**  
  ➝ *Test:* Vérifie si Neo4j trouve des films par année en utilisant un film de référence.

- **List movies featuring at least 3 actors who have won an Oscar.**  
  ➝ *Test:* L'agent doit croiser des données sur les acteurs et leurs récompenses.

- **Which sci-fi movies have a runtime longer than 2.5 hours?**  
  ➝ *Test:* Filtrer les films d’un genre spécifique selon leur durée.

## 🟡 Analyse des relations entre acteurs et réalisateurs
- **Which directors have worked with both Leonardo DiCaprio and Tom Hardy?**  
  ➝ *Test:* Vérifie si Neo4j peut croiser plusieurs relations [:DIRECTED] et [:ACTED_IN].

- **Find actors who have played a superhero in at least two different franchises.**  
  ➝ *Test:* Vérifie si l'agent peut regrouper des films par franchises différentes.

- **Which actor has worked with the most different directors?**  
  ➝ *Test:* Vérifie si l'agent peut faire un classement en comptant des relations dans Neo4j.

## 🟠 Requêtes basées sur des descriptions (recherche vectorielle)
- **Find movies about time travel but NOT featuring robots.**  
  ➝ *Test:* La recherche vectorielle doit identifier des films correspondant au thème, tout en excluant des éléments.

- **Which movies have a similar plot to "Blade Runner"?**  
  ➝ *Test:* Vérifie si l'index vectoriel est bien utilisé pour la recherche de films similaires.

## 🔴 Résolution d'ambiguïtés & Contextualisation
- **(First question) Who directed "Batman"?**  
- **(Follow-up question) And who played the Joker in that movie?**  
  ➝ *Test:* L'agent doit se souvenir du film mentionné précédemment pour répondre.

- **What is the most recent movie starring both Margot Robbie and Ryan Gosling?**  
  ➝ *Test:* Vérifie si l’agent peut trier les films par date de sortie.

## 🟣 Détection et gestion des erreurs
- **List movies directed by "John Doe".**  
  ➝ *Test:* Que se passe-t-il si la personne n'existe pas dans la base ?  
  ✅ L'agent devrait répondre *"No data found in the database"* au lieu de planter.

- **Find the budget of the movie "Inexistent Movie 3000".**  
  ➝ *Test:* L'agent gère-t-il bien une demande sur un film non référencé ?

## 🔵 Créativité & Recommandations avancées
- **Suggest a list of movies with a similar tone to "Joker" and "Taxi Driver".**  
  ➝ *Test:* Vérifie si l’agent est capable de trouver des films psychologiques similaires.

- **What are the top 5 highest-rated movies directed by female directors?**  
  ➝ *Test:* Vérifie si l’agent peut filtrer par genre et classer les résultats par note.

## 🟤 Génération et analyse de tendances
- **Which actor has appeared in the most Oscar-winning movies?**  
  ➝ *Test:* Vérifie si l'agent peut compter des films liés aux Oscars.

- **Which decade had the most horror movies released?**  
  ➝ *Test:* Vérifie si l'agent peut regrouper les films par décennie et faire des stats.

---

Who is the CEO of Neo4j?

https://raw.githubusercontent.com/neo4j-graphacademy/courses/refs/heads/main/asciidoc/courses/llm-chatbot-python/modules/3-tools/lessons/1-vector-tool/reset.cypher
