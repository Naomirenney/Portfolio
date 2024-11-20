


def compound_interest():
    starting_balance= float(input("Please enter your initial investment: "))
    interest_rate= float(input("Please enter your interest rate: "))
    contribution= float(input("Enter your monthly contributions: "))
    months=int(input("Enter the amount of months to show a list of income for every month "))
    end=0
    n=0

    for i in range(months):
        n+=1
        end+= starting_balance*interest_rate+contribution
        print(f"Month {n}: {end}")

#call compund_interest function
compound_interest()

