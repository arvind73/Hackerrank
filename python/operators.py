#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    totalcost = meal_cost + tip + tax
    return "Total cost of the meal is " + str(round(totalcost))

if __name__ == '__main__':
    meal_cost = float(input("Enter the meal cost: "))

    tip_percent = int(input("Enter the tip in percent: "))

    tax_percent = int(input("Enter the tax in percent: "))

    print(solve(meal_cost, tip_percent, tax_percent))
