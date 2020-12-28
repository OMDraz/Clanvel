import math 

example_value = (63/25)*(17+15*math.sqrt(5)) / (7+15*math.sqrt(5))
mantissa_fraction, exponent = math.frexp(exmaple_value)
mantissa_whole = int(mantissa_fraction*2**53)
message_text = f'the internal representation is {mantissa_whole:d}/2**53*2**{exponent:d}'
print(message_text)
