
data_lines= open("newfile.txt", "w")
data_lines.write("""aaaaaaaaaaaaaaaaaaaaaaaa
98ha97bjnk80j9k9kstr04pb5b84r961fqcet4bdr02fkv0d68e34d17qntj
wpq20da0wr035z7m42wnqb25p3w7jebi27280ub4374076o1660mz45m
3mkv5b3p632x1ie2l6mgnjrjwr04h2q645v4m5y2er5zydt9ea9d99""")


try:
       with open("newfile.txt", "r") as data_lines:
        total_sum = 0 #Initializing total sum to calculate total numeric 
        total_alpha = 0 #Initializing total sum to calculate total non-numeric 

        for line in data_lines:
            numeric_part = ''.join(value for value in line if value.isdigit()) #performs several steps in Python to extract the numeric part from a string (line)

            # Check for empty numeric part to handle lines with only digits
            if not numeric_part:
                print("Line only contains non-numeric: ",line )  #line.strip()
                total_alpha += 1  # Count lines with only digits
                continue  # Skip to the next line for better efficiency
           
            first_digit = numeric_part[0] #To get first digit from numeric charcaters 
            last_digit = numeric_part[-1] # to get last digit from numeric charcaters

            # Ensure both digits are valid before conversion
            if first_digit.isdigit() and last_digit.isdigit():
                number = (first_digit + last_digit) #converts into int and Adding first and last digits 
                total_sum += int(number) #Adding the numbers
                print("First and last numeric:", number)

            else:
                print(line, "Line contain non-numeric characters.") #Non-numeric characters
                total_alpha += 1  # Count lines without digits

except FileNotFoundError:
    print("Error: File '293.txt' not found.")

else:
    print("Total sum of numeric digits:", total_sum)
    print("Total lines with non-numeric characters:", total_alpha)
    Total=total_sum+total_alpha
    print(Total)