"A Conversion python program for hw01"

def kg_to_lbs(number, measurement):
    """1kg = 2.20462lbs, multiply in this variation"""
    response = "Error"
    if measurement == 'kg' and is_valid_number(string = number):
        digit = float(number)
        conversion = digit * 2.20462
        response = f"{conversion:.2f} lbs"
    return response

def lbs_to_kg(number, measurement):
    """1kg = 2.20462lbs, divide in this variation"""
    response = "Error"
    if measurement == "lbs" and is_valid_number(string = number):
        digit = float(number)
        conversion = digit * (1 / 2.20462)
        response = f"{conversion:.2f} kg"
    return response

def f_to_c(number, measurement):
    """Celcius = (F - 32) * 5/9"""
    response = "Error"
    if measurement == "f" and is_valid_number(string = number):
        digit = float(number)
        conversion = (digit - 32) * (5/9)
        response = f"{conversion:.2f} c"
    return response

def c_to_f(number, measurement):
    """Fahrenheit = (C * 9/5) + 32 """
    response = "Error"
    if measurement == "c" and is_valid_number(string = number):
        digit = float(number)
        conversion = (digit * (9/5)) + 32
        response = f"{conversion:.2f} f"
    return response

def ft_to_m(number, measurement):
    """Meter = ft * .304"""
    response = "Error"
    if measurement == "ft" and is_valid_number(string = number):
        digit = float(number)
        conversion = digit * .304
        response = f"{conversion:.2f} m"
    return response

def m_to_ft(number, measurement):
    """ft = meter / .304"""
    response = "Error"
    if measurement == "m" and is_valid_number(string = number):
        digit = float(number)
        conversion = digit * (1 /.304)
        response = f"{conversion:.2f} ft"
    return response

def ac_to_sqft(number, measurement):
    """sqft = ac * 43560"""
    response = "Error"
    if measurement == "ac" and is_valid_number(string = number):
        digit = float(number)
        conversion = digit * 43560
        response = f"{conversion:.2f} sqft"
    return response

def sqft_to_ac(number, measurement):
    """ac = sqft / 43560"""
    response = "Error"
    if measurement == "sqft" and is_valid_number(string = number):
        digit = float(number)
        conversion = digit / 43560
        response = f"{conversion:.2f} ac"
    return response

def is_valid_number(string):
    """Checks only 1 decimal, decimal at start, and only digits"""
    if string.count('.') > 1:
        return False
    if string == '' or (string[0] == '-' and string[1:] == ''):
        return False
    for i, char in enumerate(string):
        if char == '.':
            if i in (0, len(string) - 1):
                return False
        elif not char.isdigit() and not (char == '-' and i == 0):
            return False
    return True

if __name__ == "__main__":
    conversion_dict = {
        0: "kg",
        1: "lbs",
        2: "f",
        3: "c",
        4: "ft",
        5: "m",
        6: "ac",
        7: "sqft",
    }
    function_dict = {
        0: kg_to_lbs,
        1: lbs_to_kg,
        2: f_to_c,
        3: c_to_f,
        4: ft_to_m,
        5: m_to_ft,
        6: ac_to_sqft,
        7: sqft_to_ac
    }
    input_to_convert = input("Insert a numerical value then a space then the measurement: ")
    inputs = input_to_convert.split()
    UNIT = str(inputs[1])
    if len(inputs) == 2 and is_valid_number(string = inputs[0]):
        KEY = 0
        FLAG = False
        while KEY < 8 and FLAG is False:
            if conversion_dict[KEY] == UNIT:
                FLAG = True
                break
            KEY+= 1
        if FLAG:
            output = function_dict[KEY](number = inputs[0], measurement = conversion_dict[KEY])
            print(output)
        else:
            print("Incorrect formatting")
    else:
        print("Incorrect formatting")
