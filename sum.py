def sum_of_digit(num):
    sum = 0
    for value in str(num):
        sum += int(value)
    return sum
num = int(input("Enter the number:"))
print(sum_of_digit(num))

