./bin/spark-shell --conf spark.neo4j.bolt.password=password --packages neo4j-contrib:neo4j-spark-connector:2.2.1-M5

https://dzone.com/articles/neo4j-with-scala-awesome-experience-with-spark

 import org.neo4j.spark._
 import org.apache.spark.graphx._
 import org.apache.spark.graphx.lib._

 val neo = Neo4j(sc)

 val graphQuery = """MATCH (n)-[r]->(m) RETURN id(n) as origin,id(m) as destination, r.distance as distance"""

 val graph: Graph[Long, Long] =neo.rels(graphQuery).partitions(1).batch(100).loadGraph

//  
val rowRDD = neo.cypher("MATCH (n:org) RETURN n.name as name limit 10").loadRowRdd
// 
val df = neo.cypher("MATCH (n)-[r]->(m) RETURN n.name as origin, m.name as destination, r.distance as distance").loadDataFrame

val rdd = neo.cypher("MATCH (n)-[r]->(m) RETURN n.name as origin, m.name as destination, r.distance as distance").loadRdd