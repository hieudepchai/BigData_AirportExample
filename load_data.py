# import pandas library to read csv into DataFrame
import pandas as pd
# import py2neo library to connect and load data to Neo4j Graph
from py2neo import Graph, Node, Relationship
#load data from csv file to dataframe airportDF
airportDF = pd.read_csv("rita2014jan.csv")
#declare a graph variable which connects to Neo4j Graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
#clear all graph data ( if existed)
graph.delete_all()
#iterate rows in airportDF
for index, row in airportDF.iterrows():
    #create origin node which is the column 'origin' in airportDF and its label is "org"
    node_a = Node("airport", name=row['origin'])
    #create destination node which is the column 'dest' in airportDF and its label is "dest"
    node_b = Node("airport", name=row['dest'])
    #create a relationship between those node, label it as "dist" and add a property "distance" which is the column dist in airportDF 
    rel = Relationship(node_a,"dist", node_b, distance=row['dist'])
    #merge the relationship into the graph variable
    graph.merge(rel, "airport", "name")
    
