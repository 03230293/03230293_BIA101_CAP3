data_lines=open("293.txt", "r")
print(data_lines)


try:
    total_sum = 0
    for line in data_lines:
        numeric_part = ''.join(value for value in line if value.isdigit())

            # Check if any digits were found
        if numeric_part:
            first_digit = numeric_part[0] if numeric_part else None
            last_digit = numeric_part[-1] if numeric_part else None

                # Check if both digits are valid
            if first_digit is not None and last_digit is not None:
                number = int(first_digit + last_digit)
                print("First and last numeric in a line:", number)
                total_sum += number  # Add the extracted number to the sum
                # print(total_sum)

        else:
            print("Line only contains digits at the beginning/end", numeric_part)
                # total_sum += number  # Add the extracted number to the sum
                # print(total_sum)

       
# except ValueError:
#         print(line," it doesn't add becuase it is non-numeric characters")
except FileNotFoundError:
    print("Error: File '293.txt' not found.")

# except (IOError, OSError) as e:  # Catch other potential file I/O errors
#     print("Error: An error occurred while accessing the file:", e)

except ValueError:
    print(data_lines, "it doesn't add because it is non-numeric characters")

else:
    print(total_sum)