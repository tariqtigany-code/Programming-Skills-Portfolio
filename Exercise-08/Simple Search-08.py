# Create a list of names 
names = ["Jake" ,"Zac", "Ian", "Ron", "Sam", "Dave"]
#Ask the user for the name 
search_name=input("Enter the name of person : ")

# check if the name is in the list 
if search_name in names :
    print(f"{search_name} was found ")

else : 
    print(f"{search_name} wasnt found ")

    
