# Github Repo link: https://github.com/03230293

#Sonam Peldon
#BBI A
#Student ID Number: 03230293

# REFERENCES
# Gemini. (2024, May 24). Gemini. Retrieved from gemini.google.com: https://geminigoogle.com/app/dd0591678c7f620b
# BroCode.( 2020, Dec  21). Python exception handling. YouTUbe.https://youtu.be/j_q6NGOwDJo?si=AYf6plM9KSZdg_SG


# SOLUTION
# Solution Score: <total sum: Sum of Numeric digits: 488043
#Numbers of alphabetic characters only in line: 0
#Total index: 488043>
################################

def read_input():  
    # Opens the file "293.txt" in read mode
    file = open("293.txt", "r")
    # Prints the file object
    print(file)
    # Reads the contents of the file
    read_file = file.read()
    # Prints the contents of the file
    print(read_file)
    # Closes the file
    file.close()

# Calls the read_input function to read and print the contents of the file
read_input()

# Defines a function to calculate the index
def My_index_calculation(Filename):
    # Checks if the provided filename is a string and not empty
    if not isinstance(Filename, str) or not Filename:
        # Raises an error if the filename is invalid
        raise ValueError("Invalid filename provided. Please enter a non-empty string.")

    # Here are the calculation parts to get the total number of the index
    try:
        # Opens the file with the provided filename in read mode
        with open("293.txt", "r") as data_lines:
            # Initializes variables to calculate the total numeric and alphabetic characters
            total_numeric = 0
            total_alphabetic_char_in_line = 0
            
            # Iterates over each line in the file
            for line in data_lines:
                # Extracts the numeric part from the line
                numeric_digits = ''.join(value for value in line if value.isdigit())

                # Checks if the line contains only non-numeric characters
                if not numeric_digits:
                    # Prints the line and a message indicating it contains only non-numeric characters
                    print("Line only contains non-numeric: ", line)
                    continue  # Skip to the next line if it contains only non-numeric characters
            
                # Gets the first and last digits from the numeric part
                first_digit = numeric_digits[0]
                last_digit = numeric_digits[-1]

                # Checks if both digits are valid before conversion
                if first_digit.isdigit() and last_digit.isdigit():
                    # Adds the first and last digits and converts them to an integer
                    numbers_in_line = first_digit + last_digit
                    total_numeric += int(numbers_in_line)
                    # Prints the first and last numeric digits from the line
                    print("First and last numeric:", numbers_in_line)
                 
                 # Handle lines with no numeric digits
                if not numeric_digits:
                    # Prints the line and a message indicating it contains no numeric digits
                    print ("Line only contains non-numeric: 0", line)
                    # Returns 0 for lines with no numeric digits
                    return 0

    except FileNotFoundError: # Handles file not found error  
        print("Error: File not found.")

    except ValueError as e:  # Handles value error
        print(e)
 
    finally:
        # Prints the sum of numeric digits
        print("Sum of Numeric digits:", total_numeric)
        # Prints the total number of alphabetic characters in the file
        print("Numbers of alphabetic characters only in line :", total_alphabetic_char_in_line)
        # Calculates the total index by adding the total numeric and alphabetic characters
        Total_index = total_numeric + total_alphabetic_char_in_line
        # Prints the total index
        print(Total_index)
        # Closes the file
        data_lines.close()

# Calls the My_index_calculation function with the filename "293.txt"
My_index_calculation("293.txt")
