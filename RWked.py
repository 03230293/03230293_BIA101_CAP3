data_lines=open("293.txt", "r") #reading the text 
print(data_lines)

def process_and_sum_lines(data_lines):
  total_sum = 0
  for line in data_lines:
    numeric_part = ''.join(char for char in line if char.isdigit())

    # Check if any digits were found
    if numeric_part:
      try:
        # Extract first and last digits (optional for combining)
        first_digit = numeric_part[0] if numeric_part else None
        last_digit = numeric_part[-1] if numeric_part else None

        # Option 1: Combine first and last digits
        if first_digit is not None and last_digit is not None:
          number = int(first_digit + last_digit)
          print(f"Line's combined number (first & last digits): {number}")
        else:
          # Option 2: Use all extracted digits (more inclusive)
          number = int(numeric_part)
          print(f"Line's number using all digits: {number}")

        total_sum += number  # Add the extracted number to the sum
      
      except ValueError:
        print(f"'{line}' contains invalid numeric characters.")
    
    else:
      # Skip lines without digits
      print(f"Warning: Line '{line}' contains invalid numeric characters.")
      pass

  return total_sum



sum_of_numbers = process_and_sum_lines(data_lines)

if sum_of_numbers:
  print("The total sum of all numeric values in the lines is: ", sum_of_numbers)
else:
  print("No numeric values found in the lines.")
