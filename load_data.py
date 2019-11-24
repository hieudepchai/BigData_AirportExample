import pandas as pd
from py2neo import Graph, Node, Relationship
airportDF = pd.read_csv("rita2014jan.csv")

graph = Graph("bolt://localhost:7687",auth=("neo4j", "password"))
graph.delete_all()

print(airportDF)
for index, row in airportDF.iterrows():
    node_a = Node("org", name=row['origin'])
    node_b = Node("dest", name=row['dest'])
    rel = Relationship(node_a,"dist", node_b, distance=row['dist'])
    graph.merge(rel,"dist", "name")
    
