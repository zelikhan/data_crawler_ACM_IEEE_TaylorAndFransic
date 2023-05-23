from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

# Load the RDF data from the file
g = Graph()
g.parse("output.rdf", format="xml")

# Define the SPARQL queries
queries = [
    """
    PREFIX ns1: <http://example.org/ontology/>

    SELECT ?person
    WHERE {
      ?person rdf:type ns1:Person .
    }
    """,
    """
    PREFIX ns1: <http://example.org/ontology/>

    SELECT ?name
    WHERE {
      ?person rdf:type ns1:Person .
      ?person ns1:hasName ?name .
    }
    """,
    """
    PREFIX ns1: <http://example.org/ontology/>

    SELECT ?person
    WHERE {
      ?person rdf:type ns1:Person .
      ?person ns1:hasAward "ACM A. M. Turing Award" .
    }
    """,
    """
    PREFIX ns1: <http://example.org/ontology/>

    SELECT ?name ?award
    WHERE {
      ?person rdf:type ns1:Person .
      ?person ns1:hasName ?name .
      ?person ns1:hasAward ?award .
      ?person ns1:hasRegion "North America" .
    }
    """
]

# Execute the queries
for query_str in queries:
    query = prepareQuery(query_str)
    results = g.query(query)

    # Process and print the results
    for row in results:
        print(row)
    print("--------------------")

