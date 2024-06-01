from flask import Flask, render_template, request
from parser_1 import gmaps_parser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def display_data():
    location = None
    country_code = None
    all_place_details = []
    error_message = None
    if request.method == "POST":
        location = request.form.get("location")
        country_code = request.form.get("country_code")
        if location and country_code:
            scraped_data = gmaps_parser(location=location, country_code=country_code)

            try:
                list = scraped_data["scrapingResult"]["locals"]
            except Exception as e:
                error_message = f"Error scraping data: {str(e)}"
                

            for place in list:
                place_details = [place['title'], place['address'], place['website']]
                all_place_details.append(place_details)

            all_place_details=all_place_details

    return render_template("data.html", location=location, country_code=country_code, all_place_details=all_place_details, error_message=error_message)



if __name__ == "__main__":
    app.run(debug=True)
