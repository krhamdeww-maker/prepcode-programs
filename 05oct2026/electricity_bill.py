# a householder consumes 275 units of electicty. the billing systen needs to determine the number of complete groups of 50 units and the remaining units. use appropriate arithmetic operations
units = int(input("how many units are consumed by a househollder"))

complete_group = units // 50
remaining_units= units % 50

print("completed groups are:",complete_group)
print("remaining units are:",remaining_units)
