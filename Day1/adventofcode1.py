from math import floor
masses = []
file = "input.txt"

with open(file, "r") as f:
    data = f.readlines()
    for line in data:
        masses.append(int(line))

req_masses=[(floor(m/3))-2 for m in masses]
print(sum(req_masses))


def calculate_fuel(mass,prev=[]):
    prev.append(mass)#save the current mass
	fuel=floor(mass/3)-2#calculate fuel for the current mass
	if (fuel<=0): #if fuel required is >=0
	    return prev
	else:
	    return calculate_fuel(fuel,prev)
