import string
import random

def pick(_LENGTH):
    string_pool = string.ascii_letters + string.digits
    result = "" 
    for i in range(_LENGTH) :
        result += random.choice(string_pool)
    return result


while True:
    keys = f"{pick(8)}{pick(8)}{pick(8)}"
    print(keys)
    count =+ 1
    if count == 50:
        break
