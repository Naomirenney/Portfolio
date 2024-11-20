
#Financial Compound interest calculator function
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



#Vowel counting in a string function 
def count_vowels():
    sentence= input("Enter a sentence/word and I will count the vowels: ")
    
    list= "aeiouAEIOU"
    
    count=0
    
    for x in sentence:
        if x in list:
            count+=1
    print(f"There are {count} vowels in this sentence/word")
    return count


def count_consonants():
    sentence= input("Enter a sentence/word and I will count the consonants: ")

    list= "aeiouAEIOU"
    
    count=0

    for x in sentence:
        if not x in list and x.isalpha():
            count+=1
    print(f"There are {count} consonants")
    return count

#Call vowel counter and consonant counter functions
count_vowels()
count_consonants()