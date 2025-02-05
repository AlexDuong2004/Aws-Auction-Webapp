import pytest
from convert import *
"""This file has ten asserts for each conversion in the convert.py function"""

def test_kg_to_lbs():
    "Ten unit tests for the kg_to_lbs function"
    assert kg_to_lbs("false", "kg") == False 
    assert kg_to_lbs("1.0.0", "kg") == False
    assert kg_to_lbs("kg", "1") == False
    assert kg_to_lbs("1", "kog") == False
    assert kg_to_lbs(".2.5", "klms") == False
    assert kg_to_lbs("1.5", "kg") == "3.31 lbs"
    assert kg_to_lbs(".35", "kg") == "0.77 lbs"
    assert kg_to_lbs("1000", "kg") == "2204.6s lbs"
    assert kg_to_lbs("32193812948", "kg") == "70975123901.42 lbs"
    assert kg_to_lbs("0", "kg") == "0.00 lbs"