
def main():
    cpe_1_7 = [] #putting the info in an array
    
    while True: #loop for the user info
        try:
            #asking user info
            name = input("Please input the name: ")
            if not name.isalpha():
                raise
            
            age = int(input("Please input the age: "))
            if age <= 0:
                raise

            # Add the name and age as a tuple to the array
            cpe_1_7.append((name, age))

            print("The name:", name)
            print("The age:", age)

            while True:  # loop for adding more input
                add = input("Want to add more input? (yes/no): ").lower()  # to ask another info
                if add.lower() == "yes":
                    break  # to continue the outer loop
                if add.lower() == "no":
                    break
                else:
                    print("Invalid response")

        except:
            print("Error: Invalid input")

        if add.lower() == "no":
            break

    if cpe_1_7: #setting the first user as the oldest using if else
        oldest_name = cpe_1_7[0][0]
        oldest_age = cpe_1_7[0][1]
        
        for user in cpe_1_7: #comparing the first oldest to the other user info to get the oldest
            if user[1] > oldest_age:
                oldest_name = user[0]
                oldest_age = user[1]
                
        print(f"The oldest person is {oldest_name} with the age of {oldest_age}.")
    
    else:
        print("No valid input were collected")

if __name__ == "__main__":
    main()