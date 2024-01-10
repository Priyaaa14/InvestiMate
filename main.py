import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
print("Hello, This is InvestiMate. Will help you get an idea of how much of your salary you can invest in certain fields.")
name= input("May I know your good name?\n")
name=name.capitalize()
print("-----------------------------------------------------------------------------------------------")

print(f"Welcome,{name}!")
print("The investment categories available are: \n1.Stocks\n2.Bonds\n3.Real Estate\n4.Cryptocurrencies \n\nThe risk acceptance levels available are:\n1.Conservative (low)\n2.Moderate/Balanced (medium)\n3.Aggressive (high) \n\n\nIt is suggested that, if you are the only source of income (critical income) for your family, you may choose low risk tolerance.\nchella"
      "However you are free to opt your own risk tolerance\n\n")
print("-----------------------------------------------------------------------------------------------")
risk_acceptance_level=input("What is your choice of risk acceptance? Please choose from: \nLow, medium, high\n")
risk_acceptance_level=risk_acceptance_level.upper()
#print("-----------------------------------------------------------------------------------------------")

print(f"You chose {risk_acceptance_level}.Do you want to change your answer?'Y' or 'N'")
ans=input()
ans=ans.upper()
#print("-----------------------------------------------------------------------------------------------")
n=0
while n < 5:
    if ans=="N":
        print("Thanks for your answer!")
        print("-----------------------------------------------------------------------------------------------")
        break
    risk_acceptance_level=input("What is your choice of risk acceptance? Please choose from:\nLow, medium, high\n")
    risk_acceptance_level=risk_acceptance_level.upper()
    print(f"You chose {risk_acceptance_level}.Do you want to change your answer?'Y' or 'N'")
    ans=input()
    ans=ans.upper()
    print("-----------------------------------------------------------------------------------------------")
salary=input("What is your current salary? Please provide your answer in figures without punctuation.\n")
salary1=salary.isnumeric()
#print("-----------------------------------------------------------------------------------------------")
if not salary1:
   print("Invalid Input. Please re-enter")
   salary = input("What is your current salary? Please provide your answer in figures without punctuation.\n")
print(f"Your salary is {salary} and your risk tolerance is {risk_acceptance_level}")
print("-----------------------------------------------------------------------------------------------")
print("The minimum investment percentage recommended is 50% of your salary. However, you can choose your savings percentage. \n")
savings_percent=input("What is the savings percentage you want to have?\n")
savings_percent=int(savings_percent)
salary=int(salary)
savings=(savings_percent/100)*salary
savings=int(savings)
print("-----------------------------------------------------------------------------------------------")
print(f"Your savings amount is {savings}")
if risk_acceptance_level=="LOW":
    s=30
    b=50
    r=20
    stocks= (30/100)*savings
    stocks=int(stocks)
    bonds= (50/100)*savings
    bonds=int(bonds)
    real_estate=(20/100)*savings
    real_estate=int(real_estate)
    table = [['STOCKS', f"{s}%", stocks], ['BONDS', f"{b}%", bonds], ['REAL ESTATE', f"{r}%", real_estate]]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    #print(f"For conservative tolerance, you can invest:\nStocks - 30%\tBonds - 50%\tReal Estate - 20%")
    #print(f"STOCKS - {stocks}\nBONDS - {bonds}\nREAL ESTATE - {real_estate}")
    print("THANKS FOR USING INVESTIMATE. HAVE A NICE DAY!")
    y = np.array([stocks,bonds,real_estate])

    mylabels = [f"STOCKS ({s}%)", f"BONDS ({b}%)", f"REAL ESTATE ({r}%)"]
    total = np.sum(y)

    #myexplode = [0, 0.2, 0]

    plt.pie(y, labels=mylabels, autopct=lambda p: '{:.0f}'.format(p * total / 100))
    #plt.legend()
    plt.show()
elif risk_acceptance_level=="MEDIUM":
    s=40
    b=30
    r=30
    stocks= (40/100)*savings
    stocks=int(stocks)
    bonds= (30/100)*savings
    bonds=int(bonds)
    real_estate=(30/100)*savings
    real_estate=int(real_estate)
    table = [['STOCKS', f"{s}%",stocks ], ['BONDS', f"{b}%", bonds], ['REAL ESTATE', f"{r}%", real_estate]]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    #print(f"For Moderate tolerance, you can invest:\nStocks - 40%\tBonds - 30%\tReal Estate - 30%")
    #print(f"STOCKS - {stocks}\nBONDS - {bonds}\nREAL ESTATE - {real_estate}")
    print("THANKS FOR USING INVESTIMATE. HAVE A NICE DAY!")
    y = np.array([stocks,bonds,real_estate])

    mylabels = [f"STOCKS ({s}%)", f"BONDS ({b}%)", f"REAL ESTATE ({r}%)"]
    total = np.sum(y)

    #myexplode = [0.2, 0, 0]

    plt.pie(y, labels=mylabels, autopct=lambda p: '{:.0f}'.format(p * total / 100))
    plt.show()
elif risk_acceptance_level=="HIGH":
    s=60
    b=10
    c=3
    r=27
    stocks= (60/100)*savings
    stocks=int(stocks)
    bonds= (10/100)*savings
    bonds=int(bonds)
    real_estate=(27/100)*savings
    real_estate=int(real_estate)
    crypto=(3/100)*savings
    crypto=int(crypto)
    table = [['STOCKS', f"{s}%", stocks], ['BONDS', f"{b}%", bonds], ['REAL ESTATE', f"{r}%", real_estate],['CRYPTOCURRENCIES', f"{c}%", crypto]]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    #print(f"For Aggressive tolerance, you can invest:\nStocks - 60%\tBonds - 10%\tReal Estate - 27%\tCryptocurrencies - 3%")
    #print(f"STOCKS - {stocks}\nBONDS - {bonds}\nREAL ESTATE - {real_estate}\nCRYPTOCURRENCIES - {crypto}\n\n")
    print("THANKS FOR USING INVESTIMATE. HAVE A NICE DAY!")
    y = np.array([stocks,bonds,real_estate,crypto])

    mylabels = [f"STOCKS ({s}%)", f"BONDS ({b}%)", f"REAL ESTATE ({r}%)",f"CRYPTOCURRENCIES ({c}%)"]
    total = np.sum(y)

    #myexplode = [0.2, 0, 0, 0]

    plt.pie(y, labels=mylabels,autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=False)
    plt.show()
else:
    print("The given input is invalid. PLease try again.")


