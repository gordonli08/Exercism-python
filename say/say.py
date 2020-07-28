teens = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
}

tens = {
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety"
}

scale = [
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1000, "thousand"),
    (100, "hundred"),
    (1, ""),
]

def say(number):
    if number < 0 or number >= 1000000000000:
        raise ValueError('Number is out of range')

    if number < 20:
        return teens[number]
    
    ret = []
    for divisor, suffix in scale:
        #get the quotient and set the remainder to 'number' for next iteration
        quotient, number = divmod(number, divisor)

        if quotient:
            ret.append(f"{verbalize(quotient)} {suffix}")

    return " ".join(ret).strip()

def verbalize(number):
    if number < 20:
        return teens[number]
    elif number < 100:
        digit1, digit2 = divmod(number, 10)
        
        if digit2:
            return f"{tens[digit1]}-{teens[digit2]}"
        return tens[digit1]
    return f"{verbalize(number//100)} hundred {verbalize(number%100)}"
    
print(say(0))