masses = []
fuel_sum=0
file = r"C:\Users\Jan\Documents\input.txt"
from math import floor

def fuel_calculation(mass,fsum=0):
    fuel=floor(mass/3)-2
    if fuel <= 0:
        return fsum
    else:
        fsum+=fuel
        return fuel_calculation(fuel, fsum)
    
with open(file, "r") as f:
    data = f.readlines()
    for line in data:
        masses.append(int(line))

for m in masses:
    #fuel=m
    #while fuel > 0:
    #    fuel=floor(fuel/3)-2
    #    fuel_sum+=fuel
    fuel_sum+=fuel_calculation(m)

print("Insgesamter Treibstoff ",fuel_sum)
print("Ergebnis von 14", fuel_calculation(14))
print("Ergebnis von 1968", fuel_calculation(1968))
print("Ergebnis von 100756", fuel_calculation(100756))