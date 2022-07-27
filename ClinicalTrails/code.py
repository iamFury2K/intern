import requests
import csv
url = '''
https://clinicaltrials.gov/api/query/full_studies?expr=ADHD&fmt=JSON
'''
data = requests.get(url)
json_file = data.json()
print(json_file)
    

            

