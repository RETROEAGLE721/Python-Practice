import requests
from pprint import pprint
import json 

try:
    he = requests.get("http://127.0.0.1:8000/")
    pprint(he.json())
    josn_output = json.dumps(he.json())
    print(josn_output)
except Exception as e:
    print(e)