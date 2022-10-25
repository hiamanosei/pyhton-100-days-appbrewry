#Write your code below this row 👇

def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return "FizzBuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"
    else:
        return input


for num in range(1, 101):

    print(fizz_buzz(num))
