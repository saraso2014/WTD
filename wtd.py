import random
import csv
with open('data.csv', newline='') as csvfile:


animals = ["Snake","Jaguar","Cougar"]
choice = random.choice(animals)
print(choice)