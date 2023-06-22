import pytest
import io
import sys
from helpers.calc import calcDistance, getPlaceId


def test_distance():
    assert(calcDistance("201 E Armory Ave", "1205 S 4th St") == "2 mins")


def test_placeID():
    assert(getPlaceId("1205 S 4th St") == 'ChIJWy5x_TrXDIgRoxTMj0B1Oag')

def test_ratingRestaurant():
    assert(ratingRestaurant("1205 S 4th St") <= 5)


test_placeID()
