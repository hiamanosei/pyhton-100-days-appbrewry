# Write your code below this line 👇
#Self code
def prime_checker(number):
    if number == 1:
        check = "prime"
    elif number == 2:
        check = "prime"
    elif number == 3:
        check = "prime"
    elif number == 5:
        check ="prime"
    elif number % 2 == 0 or number % 3 == 0:
        check = " not prime"
    else:
        check = "prime"
    return check


# Write your code above this line 👆

# Do NOT change any of the code below👇

n = int(input("Check this number: "))

prime_checker(number=n)



