
# Create the dictonary mapping  month number to days 
Month_Days ={ 
    1 : 31 ,
    2 : 28 , 
    3 : 31 , 
    4 : 30 , 
    5 : 31 , 
    6 : 30 , 
    7 : 31 , 
    8 : 31 , 
    9 : 30 , 
    10 : 31 ,
    11 : 30 ,
    12 :31 
}

# Ask the user for input 
month = int(input("Enter the month number (1 - 12) :"))

if 1 <= month <=12 : # check if  input is correct 
    if month ==2 : # hndle leap year (advanced requirment )
        is_leap = input("Is it a leap year ?()").strip().lower()
        if is_leap == "yes":
            print("February has 29 days")
        else : 
            print('February has 28 days')
    else :  # ouput the month mapping to days 
        print(f"there are {Month_Days[month]}  days in this month ") 
else :  
    print("wrong month number ..please Enter a number between 1 and 12")        
