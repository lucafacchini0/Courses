# Create a program that checks numbers from 1 to 10 and print only the even number, then print how many numbers are odd
cont = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        cont = cont + 1

print(f"There are {cont} even numbers")