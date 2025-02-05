import pytest
from convert import *
"""This file has ten asserts for each conversion in the convert.py function"""

def test_kg_to_lbs():
    "Ten unit tests for the kg_to_lbs function"
    assert kg_to_lbs("false", "kg") == 'Error'
    assert kg_to_lbs("1.0.0", "kg") == 'Error'
    assert kg_to_lbs("kg", "1") == 'Error'
    assert kg_to_lbs("1", "kog") == 'Error'
    assert kg_to_lbs(".2.5", "klms") == 'Error'
    assert kg_to_lbs("1.5", "kg") == "3.31 lbs"
    assert kg_to_lbs("0.35", "kg") == "0.77 lbs"
    assert kg_to_lbs("1000", "kg") == "2204.62 lbs"
    assert kg_to_lbs("32193812948", "kg") == "70975123901.42 lbs"
    assert kg_to_lbs("0", "kg") == "0.00 lbs"

def test_lbs_to_kg():
    "Ten unit tests for the lbs_to_kg function"
    assert lbs_to_kg("true", "kg") == 'Error'
    assert lbs_to_kg("5.2.1", "lbs") == 'Error'
    assert lbs_to_kg("lbs", "1") == 'Error'
    assert lbs_to_kg("2", "lb") == 'Error'
    assert lbs_to_kg(".3.1", "lmbs") == 'Error'
    assert lbs_to_kg("3.31", "lbs") == "1.50 kg"
    assert lbs_to_kg("0.77", "lbs") == "0.35 kg"
    assert lbs_to_kg("2204.62", "lbs") == "1000.00 kg"
    assert lbs_to_kg("70975123901.42", "lbs") == "32193812948.00 kg"
    assert lbs_to_kg("0", "lbs") == "0.00 kg"