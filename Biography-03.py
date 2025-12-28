# we use input() to get data from user 
Name =input("Enter your Name : ")
Hometown=input("Enter your Hometown please : ")

# we convert variable age  to inter because age is a number if user enter string it will be Error 
Age =int(input("Enter your Age : "))


#STORE Data in Dictonary 
my_biography = { 
    "name": Name , 
    "age" : Age , 
    "hometown" : Hometown 
}

# printing anything 
#\n means New Line 
print(f"Name : {my_biography["name"]}\nHometown : {my_biography["hometown"]}\nAge : {my_biography["age"]}")


