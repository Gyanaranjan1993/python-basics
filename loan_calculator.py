#Get details of the loan
money_owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is the annual percentage rate (APR) of the loan?\n'))
payment = float(input('What is the monthly payment you can afford?\n'))
months = int(input('How many months do you want to pay off the loan?\n'))

monthly_rate = apr / 100 / 12

for month in range(months): 
#Calculate interest to pay
    interest = money_owed * monthly_rate

#Add in interest
    money_owed += interest

    if(money_owed < payment):
        print('The last payment amount is', money_owed)
        print('You have paid off the loan in', month + 1, 'months.')
        break
# Make Payment
    money_owed -= payment
    print('Paid', payment, 'of which', interest, 'was interest.', end=' ')
    print('Now you owe', money_owed, 'dollars.')