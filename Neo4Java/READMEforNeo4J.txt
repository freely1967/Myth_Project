basically its an intro for people to make the same graphdatanbase

update, use this instead of last one , this contain the myth_query1358 as datasource format


LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/freely1967/Myth_Project/refs/heads/main/myth_query1358with.csv' AS row
MERGE (a:Entity {id: row.char1Label})
  ON CREATE SET a.label = row.char1Label, a.type = row.char1Type
MERGE (b:Entity {id: row.char2Label})
  ON CREATE SET b.label = row.char2Label, b.type = row.char2Type;



LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/freely1967/Myth_Project/refs/heads/main/myth_query1358with.csv' AS row
MATCH (a:Entity {id: row.char1Label})
MATCH (b:Entity {id: row.char2Label})
MERGE (a)-[:RELATED {type: row.relationLabel}]->(b);

MATCH (a)-[r]->(b)
RETURN a, r, b ;





______________________________________________________________________________________
______________________________________________________________________________________
______________________________________________________________________________________
______________________________________________________________________________________
______________________________________________________________________________________
OLD VERSION: 


Step 1: Access Neo4j Online

Go to Neo4j Sandbox (https://sandbox.neo4j.com/) - this is free and doesn't require installation
Create an account or log in
Click "New Project" and select "Blank Sandbox"
Wait for your instance to be created (takes 1-2 minutes)

Step 2: Access Neo4j Browser

Once your sandbox is ready, click "Open" next to "Neo4j Browser"
You'll see the Neo4j Browser interface with a command line at the top

Step 3: Load Your Data
Since your files are on GitHub, you can load them directly using Cypher queries. Run these commands one by one in the Neo4j Browser:
Load Nodes:

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/freely1967/Myth_Project/refs/heads/main/Neo4Java/nodes.csv' AS row
CREATE (n:Character {id: row.id, label: row.label, type: row.type})

Load Relationships:

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/freely1967/Myth_Project/refs/heads/main/Neo4Java/relationships.csv' AS row
MATCH (start:Character {id: row.start_id})
MATCH (end:Character {id: row.end_id})
CREATE (start)-[:RELATED {type: row.type}]->(end)


Note: You'll need to add Zeus to your nodes.csv file first, or create it manually:

CREATE (zeus:Character {id: 'Zeus', label: 'Zeus', type: 'Olympian god'})

Step 4: Visualize Your Graph
Run this query to see your complete graph:

MATCH (n)-[r]->(m) RETURN n, r, m

Or to see all nodes and relationships:

MATCH (n) OPTIONAL MATCH (n)-[r]->(m) RETURN n, r, m

Step 5: Customize Visualization






















