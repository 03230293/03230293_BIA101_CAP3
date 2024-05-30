# Github Repo link: https://github.com/03230293

#Sonam Peldon
#BBI A
#Student ID Number: 03230293

# REFERENCES

# Links that you referred while solving 
# the problem

# http://link.to.an.article/video.com 
################################

# SOLUTION
# Solution Score: <total sum: Sum of Numeric digits: 246816
#Numbers of alphabetic characters only in line : 50
#Total index: 246866>
################################


def My_index_calculation(Filename):
    if not isinstance(Filename, str) or not Filename:
        raise ValueError("Invalid filename provided. Please enter a non-empty string.")

    try:
        with open("293.txt", "r") as data_lines : #to read a text file
            
            total_numeric = 0 #Initializing total sum to calculate total numeric 
            total_alphabetic_char_in_line = 0 #Initializing total sum to calculate total non-numeric 
            
            # Using forloop to get each characters from text file.
            for line in data_lines:
                numeric_digits = ''.join(value for value in line if value.isdigit()) #to extract the numeric part from a string (line)

                # Check for empty numeric part to handle lines with only digits
                if not numeric_digits:
                    print("Line only contains non-numeric: ",line )  #line.strip()
                    total_alphabetic_char_in_line += 1  # Count lines with only digits
                    continue  # Skip to the next line for better efficiency
            
                first_digit = numeric_digits[0] #To get first digit from numeric charcaters 
                last_digit = numeric_digits[-1] # to get last digit from numeric charcaters

                # Ensure both digits are valid before conversion
                if first_digit.isdigit() and last_digit.isdigit():
                    numbers_in_line = first_digit + last_digit #Adding first and last digits 
                    total_numeric += int(numbers_in_line) #converting digits into int and Adding the numbers
                    print("First and last numeric:", numbers_in_line)

                else:
                    print(line, "Line contain non-numeric characters.") #Non-numeric characters
                    total_alphabetic_char_in_line += 1  # Count lines without digits


    except FileNotFoundError: #if file is not found, it will be executed  
        print("Error: File not found.")

    except ValueError as e:  #If name error found , it will get printed 
        print(e)
 
#if there is no error found, then we will calculate the the total numeric, total alphabetic characters  in line and adding of bith digits
    # else:
    finally:
        print("Sum of Numeric digits:", total_numeric) # prints only the s 
        print("Numbers of alphabetic characters only in line :", total_alphabetic_char_in_line) #prints the  total only  total alphabetic characters in line
        Total_index=total_numeric+total_alphabetic_char_in_line # total Combination of all digits and non-digits 
        print("Total index: ", Total_index)
        data_lines.close()
        
My_index_calculation("293.txt")
