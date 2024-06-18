from db_connect.db_connect import get_neo4j_driver

driver = get_neo4j_driver()

# Getting a random quote by a given character
def get_quote_helper(tx, name):
    query = """
            WITH timestamp() AS currentTimestamp
            MATCH (author:Author {name: $name})-[:HAS_QUOTE]->(quote:Quote)
            WITH quote, rand() * toFloat(currentTimestamp) AS randomOrder
            RETURN quote
            ORDER BY randomOrder
            LIMIT 1
            """
    return tx.run(query, name=name).data()[0]

def get_quote(character):
    with driver.session() as session:
        quote = session.execute_read(get_quote_helper, character)
    quote = quote["quote"]
    return quote