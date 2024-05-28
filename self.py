data_lines=open("293.txt", "r")
print(data_lines)

try:
    total_sum = 0
    for line in data_lines:
        numeric_part = ''.join(value for value in line if value.isdigit())
        
        first_digit = numeric_part[0] if numeric_part else None
        last_digit = numeric_part[-1] if numeric_part else None
                
                # Check if both digits are valid
        if first_digit is not None and last_digit is not None:
          number = int(first_digit + last_digit)
          print("First and last numeric in a line:", number)
          
          total_sum += number  # Add the extracted number to the sum

        else:
            print( line, "Line only contains digits at the beginning/end.")

except FileNotFoundError:
    print("Error: File '293.txt' not found.")

else:
    print(total_sum)