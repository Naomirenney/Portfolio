
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

# countng number of ducks in a string where 'duck'=1 and 'ducks'=2
def ducks():
    num=0
    string= input("Enter the sentence to count the amount of ducks: ")
    words= string.lower().split()
   
    
    for ducks in words:
        
        if ducks.strip("!,.")== "duck":
            num+=1
            
        elif ducks.strip("!,.") == "ducks":
            num+=2
        
    print(f"There are {num} ducks in this sentence.")
   
    return num
#call duck function
ducks()

#function to check if a string is a palindrome
def palindrome():
    
    string= input("Enter the sentence/word to check if it's a palindrome: ")
    string= string.lower().replace(" " ,"")
    if string== string[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
#call function
palindrome()

#collatz conjecture

def collatz():

    n= input("Enter the starting number to execute the collatz conjecture:")
    
    if n==1:
        print(n)
        return [n]
        
    if n%2==0:
        
        print(n)
        return [n]+ collatz(n//2) 
    else:
        print(n)
        return [n]+collatz(n*3+1)

collatz()

#binary to base 10
import math

def parse_binary():
    
    binary=input("Enter the binary number: ")
    int_result = 0
    for r in range(len(binary)):
        if binary[r] == "1":
            int_result += 2**(len(binary) - r -1)
    print(f"The base 10 number is: {int_result}")
    return int_result
parse_binary()


#sorting sublists within a list e.g list= [["Fen", 3], ["Bart", 5], ["Oscar", 4], ["Homer", 2]]
def sort_people():
    people= input("Enter your list to be sorted")
    people.sort(key=lambda person:person[1])
    print(people)
    return people

sort_people()