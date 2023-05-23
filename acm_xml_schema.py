import csv
from rdflib import Graph, Literal, Namespace, RDF, URIRef
import urllib.parse
# Read the CSV file
csv_file = r'ACM.csv'
# Define your namespace
ns = Namespace('http://example.org/ontology/')
g = Graph()
with open(csv_file, 'r') as file:
 reader = csv.DictReader(file)
 for row in reader:
    Name = row['Name']
    Awards = row['Awards']
    Year = row['Year']
    Region=row['Region']
    encoded_first_name = urllib.parse.quote_plus(Name)
    encoded_last_name = urllib.parse.quote_plus(Awards)
    encoded_first_name = urllib.parse.quote_plus(Year)
    encoded_last_name = urllib.parse.quote_plus(Region)

    instance_uri = URIRef('http://example.org/resource/' + encoded_first_name)
    g.add((instance_uri, RDF.type, ns['Person']))

    g.add((instance_uri, ns['hasName'], Literal(Name)))
    g.add((instance_uri, ns['hasAward'], Literal(Awards)))
    g.add((instance_uri, ns['hasYear'], Literal(Year)))
    g.add((instance_uri, ns['hasRegion'], Literal(Region)))

output_file = 'output.rdf'
g.serialize(output_file, format='xml')
