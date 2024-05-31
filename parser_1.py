from sc_google_maps_api import ScrapeitCloudClient
import json

def gmaps_parser(location, country_code):
        
        client = ScrapeitCloudClient(api_key='06dbfb89-957c-4263-ad72-1a016669e8f8')
        
        params = {
                "keyword": location,
                "country": country_code,
                "domain": "lk"
                }
        
        response = client.scrape(params)
        
        data = json.loads(response.text) 

        return data