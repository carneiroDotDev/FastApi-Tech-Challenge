# python3 client/main.py
import requests

filename = "size-distribution1.csv"

csv = f"./assets/{filename}"
url = 'http://localhost:8000/findmax/'

files = {'file': (csv, open(csv, 'rb'), 'text/csv')}

with open(csv, 'rb') as f:
    r = requests.post(url, files=files, verify=False)
    print(r.text)
