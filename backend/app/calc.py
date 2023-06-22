
import urllib.request
import json

maps_api_key = 'AIzaSyDLxgV4_-ZOAX2q-hDvPa05qLP27veSzJU'
restloc = ['603 E Green St, Champaign, IL 61820, USA', '708 S Goodwin Ave, Urbana, IL 61801, USA', '515 S Neil St, Champaign, IL 61820, USA']
busloc = ['First & Stadium (NW Corner)', 'ARC (North Side)', 'Fourth & Peabody (NW Corner)']


"""
Returns the distance between the origin and destination, given two placeIds.
"""


def calcDistance(origin, dest):
    originPID = getPlaceId(origin)
    destPID = getPlaceId(dest)
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=place_id:" + destPID.replace(" ", "%") + "&origins=place_id:" + originPID.replace(" ", "%") + "&key=" + maps_api_key
    print(url)
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf=8'))
    return contents["rows"][0]["elements"][0]["duration"]["text"]


"""
Returns place ID given an address. This will be used in the calcDistance function.
"""


def getPlaceId(add):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + add.replace(" ", "%") + "&inputtype=textquery&key=" + maps_api_key
    contents = json.loads(urllib.request.urlopen(url).read().decode('utf=8'))
    return contents['candidates'][0]['place_id']


def restaurantDist(loc):
    distances = []
    for i in restloc:
        distances.append(int((calcDistance(loc, i))[0:1]))
    dist = int(min(distances))
    if (dist > 20):
        return "1 (20+ mins)"
    elif (dist > 15):
        return "2 (15-20 mins)"
    elif (dist > 10):
        return "3 (10-15 mins)"
    elif (dist > 5):
        return "2 (5-10 mins)"
    else:
        return "1 (0-5 mins)"

def classDist(loc):
    dist = int(calcDistance(loc, "1401 W Green St, Urbana, IL 61801")[0:1])
    if (dist > 20):
        return "1 (20+ mins)"
    elif (dist > 15):
        return "2 (15-20 mins)"
    elif (dist > 10):
        return "3 (10-15 mins)"
    elif (dist > 5):
        return "2 (5-10 mins)"
    else:
        return "1 (0-5 mins)"

def busDist(loc):
    distances = []
    for i in busloc:
        distances.append(int((calcDistance(loc, i))[0:1]))
    dist = int(min(distances))
    if (dist > 20):
        return "1 (20+ mins)"
    elif (dist > 15):
        return "2 (15-20 mins)"
    elif (dist > 10):
        return "3 (10-15 mins)"
    elif (dist > 5):
        return "2 (5-10 mins)"
    else:
        return "1 (0-5 mins)"

print(calcDistance("201 E Armory Ave", "1205 S 4th St"))
print(busDist("1205 S 4th St"))
