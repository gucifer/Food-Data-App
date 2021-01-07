import http.client

conn = http.client.HTTPSConnection("edamam-recipe-search.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "36f705baa8msh44335f3142fd8fdp166372jsn51f840150135",
    'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com"
    }

conn.request("GET", "/search?q=butter", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
