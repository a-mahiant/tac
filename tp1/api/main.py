import requests

url = "https://www.wikidata.org/w/api.php"

while True:
    query = input("Enter entity code : ")
    if query == "quit":
        break
    else:
        params = {
        "action" : "wbsearchentities",
        "language" : "en",
        "format" : "json",
        "search" : query 
        }
        try:
            data = requests.get(url,params=params)
            print(data.json())
        except:
            print("Invalid input, try again with another one")