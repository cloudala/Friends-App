import os
from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv

def get_neo4j_driver():
    # Load environmental variables from the .env file
    load_dotenv()
    uri = os.getenv("URI")
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")

    # Create and return a Neo4j driver
    driver = GraphDatabase.driver(uri, auth=basic_auth(username, password), database="neo4j")
    return driver