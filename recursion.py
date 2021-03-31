""" QUESTION : Write a function that takes an integer N as argument which prints N (N-1) (N-2) ...1 
and then prints 1 ... n."""

number = int(input("ENTER AN INTEGER: "))


def recursion(number):
    if(number < 1):
        return
        # PRINTS N.....1
    print(number)
    # RECURSION FUNCTION
    recursion(number - 1)
    # PRINTS 1....N
    print(number)


recursion(number)
