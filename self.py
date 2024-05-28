data_lines=open("293.txt", "r") #Read a text file.
print(data_lines)

try:
        total_sum = 0 #Initializing total sum to calculate total numeric 
        total_alpha = 0 #Initializing total sum to calculate total non-numeric 

        for line in data_lines:
            numeric_part = ''.join(value for value in line if value.isdigit()) #performs several steps in Python to extract the numeric part from a string (line)

            # Check for empty numeric part to handle lines with only digits
            if not numeric_part:
                print("Line only contains non-numeric: ", line.strip())
                total_alpha += 1  # Count lines with only digits
                continue  # Skip to the next line for better efficiency
           
            first_digit = numeric_part[0] #To get first digit from numeric charcaters 
            last_digit = numeric_part[-1] # to get last digit from numeric charcaters

            # Ensure both digits are valid before conversion
            if first_digit.isdigit() and last_digit.isdigit():
                number = int(first_digit + last_digit) #converts into int and Adding first and last digits 
                total_sum += number #Adding the numbers
                print("First and last numeric:", number)

            else:
                print(line.strip(), "Line contain non-numeric characters.") #Non-numeric characters
                total_alpha += 1  # Count lines without digits

except FileNotFoundError:
    print("Error: File '293.txt' not found.")

else:
    print("Total sum of numeric digits:", total_sum)
    print("Total lines with non-numeric characters:", total_alpha)
    Total=total_sum+total_alpha
    print(Total)

try:
      with open("modified.txt", "w") as modified_file:
        total_sum = 0 #Initializing total sum to calculate total numeric 
        total_alpha = 0 #Initializing total sum to calculate total non-numeric 

        for line in data_lines:
            numeric_part = ''.join(value for value in line if value.isdigit()) #performs several steps in Python to extract the numeric part from a string (line)

            # Check for empty numeric part to handle lines with only digits
            if not numeric_part:
                print("Line only contains non-numeric: ", line.strip())
                total_alpha += 1  # Count lines with only digits
                continue  # Skip to the next line for better efficiency
           
            first_digit = numeric_part[0] #To get first digit from numeric charcaters 
            last_digit = numeric_part[-1] # to get last digit from numeric charcaters

            # Ensure both digits are valid before conversion
            if first_digit.isdigit() and last_digit.isdigit():
                number = int(first_digit + last_digit) #converts into int and Adding first and last digits 
                total_sum += number #Adding the numbers
                print("First and last numeric:", number)

            else:
                print(line.strip(), "Line contain non-numeric characters.") #Non-numeric characters
                total_alpha += 1  # Count lines without digits

except FileNotFoundError:
    print("Error: File '293.txt' not found.")

else:
    print("Total sum of numeric digits:", total_sum)
    print("Total lines with non-numeric characters:", total_alpha)
    Total=total_sum+total_alpha
    print(Total)