import math


number = input()
number = int(number)

if math.sqrt(number) == round(math.sqrt(number)):
    sqrt_number = number**(1/2)
    sqrt_number = int(sqrt_number)
else:
    sqrt_number = "-"

if round(math.pow(number, 1./3.), 1) >= round(math.pow(number, 1./3.), 7):
    crt_number = round(math.pow(number, 1/3), 2)
    crt_number = int(crt_number)
else:
    crt_number = "-"

print(f"{number} {sqrt_number} {crt_number}")