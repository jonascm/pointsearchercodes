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
orides = Graph("http://localhost:7474/db/data/")



