"A Conversion python program"

def kg_to_lbs(float):
    "1kg = 2.20462lbs"
    conversion = float * 2.20462
    response = f"{conversion:.2f} lbs"
    return response

def lbs_to_kg(float):
    return

def f_to_c(float):
    return

def c_to_f(float):
    return

def ft_to_m(float):
    return

def m_to_ft(float):
    return

def ac_to_sqft(float):
    return

def sqft_to_ac(float):
    return


if __name__ == "__main__":
    """Requesting the value then using a case-switch to choose function"""
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
    input_to_convert = input("Two decimal value with a space then the desired units in lowercase: ")
    inputs = input_to_convert.split()
    number = float(inputs[0])
    measurement = str(inputs[1])
    if len(inputs) == 2:
        key = 0
        flag = False
        while key < 8 and flag == False :
            if conversion_dict[key] == measurement:
                flag == True 
            key+= 1
        if flag:
            output = function_dict[key](float = number)
            print(output)
        else:
            print("Incorrect formatting")
    else:
        print("Incorrect formatting")
