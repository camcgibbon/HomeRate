
import urllib.request
import json

maps_api_key = 'AIzaSyDLxgV4_-ZOAX2q-hDvPa05qLP27veSzJU'
restloc = ['603 E Green St, Champaign, IL 61820, USA', '708 S Goodwin Ave, Urbana, IL 61801, USA', '515 S Neil St, Champaign, IL 61820, USA']
busloc = ['First & Stadium (NW Corner)', 'ARC (North Side)', 'Fourth & Peabody (NW Corner)']


"""
Returns the distance between the origin and destination, given two placeIds.
"""


def calcDistance(origin, dest): #returns time
    originPID = getPlaceId(origin)
    destPID = getPlaceId(dest)
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=place_id:" + destPID.replace(" ", "%") + "&origins=place_id:" + originPID.replace(" ", "%") + "&key=" + maps_api_key
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf=8'))
    return contents["rows"][0]["elements"][0]["duration"]["text"]


"""
Returns place ID given an address. This will be used in the calcDistance function.
"""


def getPlaceId(add):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + add.replace(" ", "%") + "&inputtype=textquery&key=" + maps_api_key
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf=8'))
    return contents['candidates'][0]['place_id']


print(calcDistance("201 E Armory Ave", "1205 S 4th St")) 
print(getPlaceId("1205 S 4th St"))

def restaurantDist(loc):
    distances = []
    for i in restloc:
        distances.append(int((calcDistance(loc, i))[0:1]))
    return (min(distances), "mins")

def classDist(loc):
    return calcDistance(loc, "1401 W Green StUrbana, IL 61801")

def busDist(loc):
    distances = []
    for i in busloc:
        distances.append(int((calcDistance(loc, i))[0:1]))
    return (min(distances), "mins")

#print(calcDistance("201 E Armory Ave", "1205 S 4th St"))
print(classDist("1205 S 4th St"))

"""
Returns rating for restaurants given an address. This will be used in the final ratings calculation.
"""

def ratingRestaurant(origin): 
    print("ratingRestaurant Function running")
    originPID = getPlaceId(origin)
    distance = 0
    rating = 5

    restaurantsList = ["403 E Green St","627 E Green St","623 E Green St","706 S Goodwin Ave","502 E John St"] # popular restaurants
    for restaurants in restaurantsList:
        distance += (int((calcDistance(origin, restaurants))[0:1])) # add the distance (time) between given restaurants
    rating = round((len(restaurantsList)*5) / (distance/5), 2)  # the lower the distance, the higher the rating should be
        # example : distance = 30 minutes (so 30 minutes to get to all 5 restaurants)
        # 30 / 5 = 6
        # 25 / 6 = 4.167 rating
        # example 2 : distance = 100 minutes
        # 100 /5 = 20
        # 25/20 = 1.25 rating
    if (rating > 5):
        rating = rating % 5
    return rating




print(ratingRestaurant("1205 S 4th St"))
