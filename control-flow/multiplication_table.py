# multiplication_table.py

# Ask user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10
for count in range(1, 11):
    result = number * count
    print(f"{number} * {count} = {result}")
