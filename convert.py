# Quick script to grab JSON from a Web API and spit out an Excel document

import requests
import pandas

r = requests.get('https://yourweb.api/data', headers={'Authorization': 'Bearer {YOURTOKEN}'})
    
df_json = pandas.read_json(r.text)
df_json.to_excel('convert.xlsx')
