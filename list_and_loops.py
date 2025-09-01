slangs = ['fuck', 'shit', 'bitch', 'asshole', 'cunt', 'dick', 'pussy', 'motherfucker', 'slut']
for slang in slangs:
    print(slang)

print(slangs[0])
del slangs[0]
print(slangs)   

expenses = []
for i in range(7):
    expenses.append(float(input("Enter expense for day {}: ".format(i+1))))
sum = 0
for expense in expenses:
    sum += expense

print("Total expenses: $", sum, sep="")
