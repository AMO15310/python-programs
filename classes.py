class water:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
name = 'Jake'
cost = 2200
a1 = water(name,cost)
#print(a1.name ,a1.cost)
print(f"{a1.name} should pay {a1.cost}")
