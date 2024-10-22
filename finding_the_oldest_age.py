

while True: #loop for the user info
        try:
            #asking user info
            name = input("Please input the name: ")
            
            age = int(input("Please input the age: "))
            if age <= 0:
                raise

            print("The name:", name)
            print("The age:", age)

            while True:  # loop for adding more input
                add = input("Want to add more input? (yes/no): ")  # to ask another info
                if add == "yes":
                    break  # to continue the outer loop
                if add == "no":
                    break
                else:
                    print("Invalid response")

        except:
            print("Error: Invalid input")

        if add == "no":
            break
