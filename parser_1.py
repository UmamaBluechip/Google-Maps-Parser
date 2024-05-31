import argparse
from sc_google_maps_api import ScrapeitCloudClient
import json

parser = argparse.ArgumentParser(description="Scrape Google Maps for locations/businesses")

parser.add_argument("-l", type=str, help="Keyword to search for locations")
parser.add_argument("-c", type=str, help="Country code")

args = parser.parse_args()

client = ScrapeitCloudClient(api_key='06dbfb89-957c-4263-ad72-1a016669e8f8')

params = {
    "keyword": args.l,
    "country": args.c,
    "domain": "lk"
}

response = client.scrape(params)

data = json.loads(response.text) 

print("__"*70)
print(data)

with open("output.json", 'w') as outfile:
        json.dump(data, outfile, indent=4)