age = input("Enter your age: ")
age = int(age)
decade = age // 10
age = age % 10
print("You are " + str(decade) + " decades and " + str(age) + " years old.")
