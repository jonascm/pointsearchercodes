from py2neo import Graph, Path, authenticate
from py2neo import Node
from py2neo import Relationship
import os
import uuid

# FIRST: start neo4j like this: 
# type: sudo neo4j start
# an error arises.
# type: sudo systemctl start neo4j
# now it should work (-.-)
# then go on the browser to http://localhost:7474/browser to see the database

authenticate("localhost:7474", "neo4j", "OnPoint1!")
cockepeep = Graph("http://localhost:7474/db/data/")

cockepeep.delete_all()

nicole = Node("Person", name="Nicole", age=24)
drew = Node("Person", name="Drew", age=20)

mtdew = Node("Drink", name="Mountain Dew", calories=9000)
cokezero = Node("Drink", name="Coke Zero", calories=0)

coke = Node("Manufacturer", name="Coca Cola")
pepsi = Node("Manufacturer", name="Pepsi")

cockepeep.create(Relationship(nicole, "LIKES", cokezero))
cockepeep.create(Relationship(nicole, "LIKES", mtdew))
cockepeep.create(Relationship(drew, "LIKES", mtdew))
cockepeep.create(Relationship(coke, "MAKES", cokezero))
cockepeep.create(Relationship(pepsi, "MAKES", mtdew))

cockepeep.create(nicole | drew | mtdew | cokezero | coke | pepsi)

query = """
MATCH (person:Person)-[:LIKES]->(drink:Drink)
RETURN person.name AS name, drink.name AS drink
"""
data = cockepeep.run(query)

for d in data:
    print(d)

hooann = Node("Person", name="Hoo-Ann", age=29)
cockepeep.create(Relationship(hooann, "LIKES", cokezero))

# finding stuff:
data = cockepeep.run(query)
print("Updated shiz")
for d in data:
    if d[0] == "Drew":
        print(d)


# delete relationsheeps
query = """
MATCH (a {name:"Drew"})-[r]-(b {name:"Mountain Dew"})
DELETE r
"""
cockepeep.run(query)


# create relationship for existing graph...
query = """
MATCH (a {name:"Drew"}),(b {name:"Mountain Dew"})
CREATE (a)-[r:HATES]->(b)
RETURN r
"""
cockepeep.run(query)
