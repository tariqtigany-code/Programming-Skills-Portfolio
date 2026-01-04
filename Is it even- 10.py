
#Function to Check if a number is even or odd 
def check(number): 
    if number % 2 == 0 :
        return "The number is even "
    else :
        return "The number is odd"
# Main function to handle user input and printing 
def main():
    #Ask the user for a number 
    user=int(input("Enter a number ti check if it is even or odd : "))

    # Pass the number to the function and get the result
    message=check(user)
     #print the result 
    print(message)

    #start the program 
if __name__ == "__main__":
    main()    

