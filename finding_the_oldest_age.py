

while True: #loop for the user info
        try:
            #asking user info
            name = input("Please input the name: ")
            
            age = int(input("Please input the age: "))
            if age <= 0:
                raise
        except:
            print("Error: Invalid input")
