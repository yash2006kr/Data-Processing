import random
i = 0
for i in range(10):
    a = random.random()
    print(a)

data = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
a = random.sample(data, 6)
print(a)

cars = ['BMW','Audi','Benz','Lamborghini','Minicooper']
my_car = random.choice(cars)
print(my_car)

x = random.uniform(1.5,8)
print(x)

x = random.randint(1,100)
print(x)

x = random.randrange(1,100,2)
print(x)