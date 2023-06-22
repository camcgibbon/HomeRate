import pytest
from app import mtd_api_key

def test_api_key():
    assert(mtd_api_key == "d6f508505e3c436daebe0290edce3903")

