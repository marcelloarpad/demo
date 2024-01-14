fahrenheit = 0
print("fahrenheit celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit, celsius))
    fahrenheit = fahrenheit + 25