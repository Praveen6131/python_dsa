# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# print(int(a/b))
while True:
    try:
        num = int(input("Enter a valid integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")