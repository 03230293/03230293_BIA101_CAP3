def sum_numeric_lines(filename):
  total_sum = 0
  try:
    with open(filename, 'r') as file:
      for line in file:
        # Remove leading/trailing whitespace and check if digits only
        if line.strip().isdigit():
          total_sum += int(line)

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  return total_sum

# Example usage
filename = "293.txt"
sum_of_numbers = sum_numeric_lines(filename)

if sum_of_numbers:
  print(f"The sum of numeric values in '{filename}' is: {sum_of_numbers}")
else:
  print(f"No numeric values found in '{filename}'.")


# try:
#     f= open("293.txt", "r")
#     for i in f:
#         print(i)
#     text=f.read()
#     print(text)

# Imagine we have a box (file) named "293.txt" filled with papers (lines of text).

# 1. Open the box (file) and tell it we only want to read what's inside (read mode)
try:
  file = open("293.txt", "r")  # "r" means read

# 2. We'll put the sum of the numbers we find in a basket (total_sum)
  total_sum = 0

# 3. Let's go through each paper (line) inside the box
  for numbers in file:

    # 4. Clean the paper a bit (remove any extra spaces at the beginning or end)
    nums = numbers.strip()

    # 5. Check if the paper only has numbers written on it (like 123 or 789)
    if nums.isdigit():

      # 6. If it's all numbers, convert it to a number we can add (like from "123" to 123)
      number = int(nums)

      # 7. Add this number to our basket (total_sum)
      total_sum += number

# 8. Oops! If the box (file) wasn't found, tell the user.
except FileNotFoundError:
  print("Uh oh, couldn't find the box named '293.txt'!")

# 9. Close the box (file) after we're done
finally:
  file.close()  # This line might be automatically added in some versions of Python

# 10. If we found any numbers, tell the user the sum in our basket
if total_sum:
  print(f"The sum of all the numbers in '293.txt' is: {total_sum}")

# 11. If there weren't any numbers, tell the user we didn't find any.
else:
  print("There weren't any numbers in '293.txt'.")
