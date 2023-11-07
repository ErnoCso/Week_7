# Task 3

# Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
# converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
# displays both.
# °F =°C * 1.8000+ 32.00


celsius = 38.4
fahrenheit = (celsius * 1.8000) + 32

if __name__ == "__main__":
    print(f"\nThe temperatures in Yorkshire: {celsius} °C.")
    print(f"{celsius} °C equals {fahrenheit} °F.")

# Output:

# Temperatures in Yorkshire: 38.4 °C.
# 38.4 °C equals 101.12 °F.
