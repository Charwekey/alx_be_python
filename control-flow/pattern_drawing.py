# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:            # while loop → rows
    for col in range(size):  # for loop → columns
        print("*", end="")   # print stars on the same line
    print()                  # move to the next line after each row
    row += 1                 # go to the next row
