"""This file has ten asserts for each conversion in the convert.py function"""
from convert import (kg_to_lbs, lbs_to_kg, f_to_c, c_to_f, ft_to_m, m_to_ft,
                     ac_to_sqft, sqft_to_ac)


def test_kg_to_lbs():
    "Ten unit tests for the kg_to_lbs function"
    assert kg_to_lbs("false", "kg") == 'Error'
    assert kg_to_lbs("1.0.0", "kg") == 'Error'
    assert kg_to_lbs("kg", "1") == 'Error'
    assert kg_to_lbs("1", "kog") == 'Error'
    assert kg_to_lbs(".2.5", "klms") == 'Error'
    assert kg_to_lbs("1.5", "kg") == "3.31 lbs"
    assert kg_to_lbs("-0.35", "kg") == "-0.77 lbs"
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
    assert lbs_to_kg("-2204.62", "lbs") == "-1000.00 kg"
    assert lbs_to_kg("70975123901.42", "lbs") == "32193812948.00 kg"
    assert lbs_to_kg("0", "lbs") == "0.00 kg"

def test_f_to_c():
    """Ten unit tests for the f_to_c function"""
    assert f_to_c("false", "c") == 'Error'
    assert f_to_c("1.3.0", "f") == 'Error'
    assert f_to_c("f", "1") == 'Error'
    assert f_to_c("3", "e") == 'Error'
    assert f_to_c(".4.1.2", "ef") == 'Error'
    assert f_to_c("3.2", "f") == "-16.00 c"
    assert f_to_c("-1.2", "f") == "-18.44 c"
    assert f_to_c("3128913", "f") == "1738267.22 c"
    assert f_to_c("17", "f") == "-8.33 c"
    assert f_to_c("0", "f") == "-17.78 c"

def test_c_to_f():
    """Ten unit tests for the c_to_f function"""
    assert c_to_f("false", "f") == 'Error'
    assert c_to_f("2.6.1.4", "c") == 'Error'
    assert c_to_f("c", "1") == 'Error'
    assert c_to_f("3", "v") == 'Error'
    assert c_to_f(".1.2.3.4", "vc") == 'Error'
    assert c_to_f("-16.00", "c") == "3.20 f"
    assert c_to_f("-18.44", "c") == '-1.19 f' #Rounding
    assert c_to_f("1738267.22", "c") == "3128913.00 f"
    assert c_to_f("-8.33", "c") == "17.01 f" #Rounding
    assert c_to_f("-17.78", "c") == "-0.00 f"

def test_ft_to_m():
    """Ten unit tests for the ft_to_m function"""
    assert ft_to_m("apple", "ft") == 'Error'
    assert ft_to_m("1.8.1.2", "ft") == 'Error'
    assert ft_to_m("ft", '27') == 'Error'
    assert ft_to_m("5", "m") == 'Error'
    assert ft_to_m(".2.1.4", "ft") == 'Error'
    assert ft_to_m("18", "ft") == "5.47 m"
    assert ft_to_m("-27", "ft") == "-8.21 m"
    assert ft_to_m("123456789", "ft") == "37530863.86 m"
    assert ft_to_m("0.28", "ft") == "0.09 m"
    assert ft_to_m("0", "ft") == "0.00 m"

def test_m_to_ft():
    """Ten unit tests for the m_to_ft function"""
    assert m_to_ft("pear", "ft") == 'Error'
    assert m_to_ft("7.1.2.4", "ft") == 'Error'
    assert m_to_ft("m", "90") == 'Error'
    assert m_to_ft("20", "ft") == 'Error'
    assert m_to_ft("-.2.1.4", "m") == 'Error'
    assert m_to_ft("5.47", "m") == "17.99 ft" #rounding
    assert m_to_ft("-8.21", "m") == "-27.01 ft" #rounding
    assert m_to_ft("987654321", "m") == "3248862898.03 ft"
    assert m_to_ft("0.09", "m") == "0.30 ft" #rounding
    assert m_to_ft("0", "m") == "0.00 ft"

def test_ac_to_sqft():
    """Ten unit tests for the ac_to_sqft function"""
    assert ac_to_sqft("grape", "sqft") == 'Error'
    assert ac_to_sqft("5.1.4.2.4", "ac") == 'Error'
    assert ac_to_sqft("ac", "12") == 'Error'
    assert ac_to_sqft("95", "sqft") == 'Error'
    assert ac_to_sqft(".6.5", 'ac') == 'Error'
    assert ac_to_sqft("2", "ac") == "87120.00 sqft"
    assert ac_to_sqft("-53", "ac") == "-2308680.00 sqft"
    assert ac_to_sqft("129834765", "ac") == "5655602363400.00 sqft"
    assert ac_to_sqft("0.91", "ac") == "39639.60 sqft"
    assert ac_to_sqft("0", "ac") == "0.00 sqft"

def test_sqft_to_ac():
    """ten unit test for the sqft_to_ac"""
    assert sqft_to_ac("banana", "sqft") == 'Error'
    assert sqft_to_ac("9.1.2", "sqft") == 'Error'
    assert sqft_to_ac("sqft", "1") == 'Error'
    assert sqft_to_ac("21", "ac") == 'Error'
    assert sqft_to_ac('.424.12', "sqft") == 'Error'
    assert sqft_to_ac("87120", "sqft") == "2.00 ac"
    assert sqft_to_ac("-9001", "sqft") == "-0.21 ac"
    assert sqft_to_ac("12", "sqft") == "0.00 ac" #Rounding
    assert sqft_to_ac("-67", "sqft") == "-0.00 ac" #Rounding
    assert sqft_to_ac("0.00", "sqft") == "0.00 ac"
