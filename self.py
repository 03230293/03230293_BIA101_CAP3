# f= open("293.txt", "r")
# for i in f:
#     print(i)
# data_lines=f.read()
data_lines=open("293.txt", "r")
print(data_lines)

def process_line(line):
  """Processes a line, extracting numeric parts and combining first/last digits if possible.

  Args:
    line: The line to process.

  Prints:
    The extracted numeric value (or a message if no digits found).
  """

  numeric_part = ''.join(char for char in line if char.isdigit())

  # Check if any digits were found
  if numeric_part:
    # Extract first and last characters from the numeric part
    first_digit = numeric_part[0] if numeric_part else None
    last_digit = numeric_part[-1] if numeric_part else None

    # Check if both digits are valid
    if first_digit is not None and last_digit is not None:
      # Combine and print the number
      number = int(first_digit + last_digit)
      print(f"Line's number: {number}")
    else:
      print(f"Line only contains digits at the beginning/end, using {numeric_part}.")
  else:
    print(f"Line doesn't contain any digits.")



# Process each line in the list
for line in data_lines:
  process_line(line)

