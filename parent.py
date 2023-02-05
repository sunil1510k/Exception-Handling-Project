

# Function to check Current Date time
def getDateTime() : 
    import datetime
    timestamp = datetime.datetime.now()
    currentDateTime = timestamp.strftime(" %Y-%m-%d     %H : %M")
    return currentDateTime


# Function to check check if string is palindrome or not
def palinCheck(stringName) : 

    if stringName.strip().lower()==stringName[::-1].strip().lower():
        return "ITS Palindrome"
    else:
        return "ITS NOT Palindrome"


## Function to find area of circle
        
def area_circle( r, p ) : 
    return p * r * r


# Function to check if a number is Even or Odd

def even_odd(a) : 

    if a%2  == 0 : 
        return "Even"
    else: 
        return "Odd"
    

# Function to finf Factorial

def factorial(number) : 

    fact=int(number)

    for i in range(fact-1,1,-1):
        
        fact=fact*i
    if fact==0:
        fact=1

    return fact



"""
print(f'Current Date Time = {getDateTime()}')

a=input("\n\n\n Enter a number to find its factorial: ")
print(f'Factorial Of a Number = {factorial(a)}')

 
a=input("\n\n\n Enter a string to check palindrome: ")
print(f"Performing Palin Check on {a} ::: {palinCheck(a)}")

"""










