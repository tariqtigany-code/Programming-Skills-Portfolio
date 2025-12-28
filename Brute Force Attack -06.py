# define the correct number 
correct_password = "12345"

user_input =input("Enter the password :")
#Use a while loop to repeatedly ask for the password
while user_input != correct_password : 
    print(" wrong password.Try again ")
    user_input =input("Enter the password :")
#Output the  message when correct
print("Correct password")    

