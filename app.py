from flask import Flask, render_template, request
from parser_1 import gmaps_parser
import json


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def display_data():
    location = None
    country_code = None
    scraped_data_json = None
    if request.method == "POST":
        location = request.form.get("location")
        country_code = request.form.get("country_code")
        if location and country_code:
            scraped_data = gmaps_parser(location=location, country_code=country_code)
            scraped_data_json = json.dumps(scraped_data, indent=4)

    return render_template("data.html", location=location, country_code=country_code, scraped_data_json=scraped_data_json if scraped_data_json else None)



if __name__ == "__main__":
    app.run(debug=True)
