# Create a program that checks numbers from 1 to 10 and print only the even number, then print how many numbers are odd
counter_of_swiss_coders = 0
for swiss_coder in range(1, 10):
    if swiss_coder % 2 == 0:
        print(swiss_coder)
        cont = cont + 1

print(f"dang bro, there are {counter_of_swiss_coders} SCHWEIZERS")