import csv
from rdflib import Graph, Literal, Namespace, RDF, URIRef
import urllib.parse
# Read the CSV file
csv_file = r'acm_file.xlsx'
# Define your namespace
ns = Namespace('http://example.org/ontology/')
g = Graph()
with open(csv_file, 'r') as file:
 reader = csv.DictReader(file)
 for row in reader:
    Author = row['Author']
    Award = row['Award']
    Year = row['Year']
    Region=row['Region']
    University=row['University']
    Average_Citation=row['Average_Citation']
    Publication_counts=row['Publication_counts']
    Citation_count=row['Citation_count']
    Average_Downloads=row['Average_Downloads']

    encoded_Author = urllib.parse.quote_plus(Author)
    encoded_Award = urllib.parse.quote_plus(Award)
    encoded_Year = urllib.parse.quote_plus(Year)
    encoded_Region = urllib.parse.quote_plus(Region)
    encoded_University = urllib.parse.quote_plus(University)
    encoded_Average_Citation = urllib.parse.quote_plus(Average_Citation)
    encoded_Publication_counts = urllib.parse.quote_plus(Publication_counts)
    encoded_Citation_count = urllib.parse.quote_plus(Citation_count)
    encoded_Average_Downloads = urllib.parse.quote_plus(Average_Downloads)


    instance_uri = URIRef('http://example.org/resource/' + encoded_first_name)
    g.add((instance_uri, RDF.type, ns['Person']))

    g.add((instance_uri, ns['hasName'], Literal(Author)))
    g.add((instance_uri, ns['hasAward'], Literal(Award)))
    g.add((instance_uri, ns['hasYear'], Literal(Year)))
    g.add((instance_uri, ns['hasRegion'], Literal(Region)))
    g.add((instance_uri, ns['hasUniversity'], Literal(University)))
    g.add((instance_uri, ns['hasAverage_Citation'], Literal(Average_Citation)))
    g.add((instance_uri, ns['hasPublication_counts'], Literal(Publication_counts)))
    g.add((instance_uri, ns['hasCitation_count'], Literal(Citation_count)))
    g.add((instance_uri, ns['hasAverage_Downloads'], Literal(Average_Downloads)))

output_file = 'acm_file_output.rdf'
g.serialize(output_file, format='xml')
