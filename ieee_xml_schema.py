import csv
from rdflib import Graph, Literal, Namespace, RDF, URIRef
import urllib.parse
# Read the CSV file
csv_file = r'IEEE NAMES.csv'
# Define your namespace
ns = Namespace('http://example.org/ontology/')
g = Graph()
with open(csv_file, 'r') as file:
 reader = csv.DictReader(file)
 for row in reader:
    Names = row['Book Names']
    Types = row['Book Type']
 
    encoded_book_name = urllib.parse.quote_plus(Names)
    encoded_book_type = urllib.parse.quote_plus(Types)


    instance_uri = URIRef('http://example.org/resource/' + encoded_book_name)
    g.add((instance_uri, RDF.type, ns['Books']))

    g.add((instance_uri, ns['hasBookName'], Literal(Names)))
    g.add((instance_uri, ns['hasBookType'], Literal(Types)))


output_file = 'output.rdf'
g.serialize(output_file, format='xml')
