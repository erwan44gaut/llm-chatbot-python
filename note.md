How many degrees of separation are there between Viola Davis and Kevin Bacon?
What year was The Matrix released?
What movies has Tom Hanks acted in?
Who is the CEO of Neo4j?


commande pour db :
CREATE VECTOR INDEX moviePlots FOR (m:Movie) ON (m.plotEmbedding)
OPTIONS {
  indexConfig: {
    `vector.dimensions`: 1536,  
    `vector.similarity_function`: 'cosine'  // Ou 'euclidean' selon ton cas
  }
};
