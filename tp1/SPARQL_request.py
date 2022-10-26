from datetime import datetime as dt
from SPARQLWrapper import SPARQLWrapper, JSON


endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
sparql = SPARQLWrapper(endpoint)

statement = """
SELECT DISTINCT ?person ?personLabel ?professionLabel ?genderLabel ?dobLabel
WHERE{
       ?person wdt:P106 wd:Q1930187 . # Journalist
       ?person wdt:P106 ?profession . # Profession
       ?person wdt:P21 ?gender . # Gender
       ?person wdt:P569 ?dobLabel . # Birthdate
       ?person wdt:P27 wd:Q31 . # Country of citizenship - Belgium
       SERVICE wikibase:label {bd:serviceParam wikibase:language "fr" }
}
ORDER BY ASC(?gender)
"""

sparql.setQuery(statement)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

rows = results['results']['bindings']
print(f"\n{len(rows)} Belgian journalists found\n")
print(rows[:10])