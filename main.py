import requests as r
import json

url = "https://calculated.gg/api/player/76561198830734493/ranks"

res = r.get(url).json()
print(res)

