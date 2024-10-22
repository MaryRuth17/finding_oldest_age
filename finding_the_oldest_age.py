
def main():
    cpe_1_7 = []  # putting the info in an array

    while True: # loop1: for the user info
        try:
            # asking user info
            name = input("Please input the name: ")
            if not name.isalpha():
                raise ValueError("Letters only")

            age = int(input("Please input the age: "))
            if age <= 0:
                raise ValueError("Invalid age")

            # Add the name and age as a tuple to the array
            cpe_1_7.append((name, age))

            print("The name:", name)
            print("The age:", age)

        except ValueError as error:
            print("Error:", error)
            continue

        while True:  #loop2: Asking if the user wants to add more input
            add = input("Want to add more input? (yes/no): ").lower()
            if add.lower() == "yes":
                break  
            elif add.lower() == "no":
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

        if add.lower() == "no":
            break  # Break the outer loop if the user said "no"
        
    if cpe_1_7:  # Check if any valid input was collected
        oldest_name = cpe_1_7[0][0]
        oldest_age = cpe_1_7[0][1]
            
        for user in cpe_1_7:  # comparing the first oldest to the other user info to get the oldest
            if user[1] > oldest_age:
                oldest_name = user[0]
                oldest_age = user[1]
                    
        print(f"The oldest person is {oldest_name} with the age of {oldest_age}.")

if __name__ == "__main__":
    main()