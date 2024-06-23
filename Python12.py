"""
#
# Part : python String Formatting
"""

price = 60
txt = f"price is {price} bath."
print(txt)
txt = f"price is {prce: .2f} bant."
print(txt)

price = 50
tax = 0.25
txt = f"price is {price + (price * tax)} bant."
print(txt)

price = 53000
txt = f"price is {price:,} bant."
print(txt)