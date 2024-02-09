num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


#sum of these numbers
print("The largest number is:", largest)
sum_of_numbers = num1 + num2 + num3

print("The sum of the numbers is:", sum_of_numbers)

#run a loop and show me the odd number between 39 to 60

start = 39
end = 60

print("Odd numbers between", start, "and", end, ":")

for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)