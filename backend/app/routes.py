from flask import render_template, request, session, jsonify, make_response
from app import app
from app import __init__
from app.forms import LocationForm
from app.calc import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
   # form = LocationForm()
   # if (form.validate_on_submit()):

   #     return render_template('homerate_homepage.html', form=form, uni_rating = classDist(form.location.data), food_rating = restaurantDist(form.location.data), bus_rating=busDist(form.location.process_data))
 #   return render_template('homerate_homepage.html', form=form, uni_rating = "", food_rating = "", bus_rating="")
    return render_template('index.html')


@app.route('/Home', methods=['GET', 'POST'])
def Home():
    return render_template("Home.html")

@app.route('/Contact', methods=['GET', 'POST'])
def Contact():
    return render_template("Contact.html")

@app.route('/Search-homes', methods=['GET', 'POST'])
def SearchHomes():
    return render_template("Search-homes.html", location="")

@app.route('/Search/<string:location_info>', methods=['GET', 'POST'])
def SearchHomesInfo(location_info):
    #location_info = json.loads(location_info)
    print(location_info)

    return make_response(jsonify({"uni": classDist(location_info), "food": restaurantDist(location_info), "bus": busDist(location_info)}))

@app.route('/apartment_search', methods=['GET', 'POST'])
def apartment_search():
    if request.method == 'POST':
        input = request.form.get('searchInput')
        restaurant_rating = ratingRestaurant(input)
        return restaurant_rating
    return render_template('form.html')



@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        render_template("404.html"),
        404
     )

@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        render_template("400.html"),
        400
    )

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )

if __name__=='__main__':
    app.run(debug=True)

