# with Fibonacci function a base case is required defining the first two special numbers
# neither 0 nor 1 is the sum of the previous two numbers in the sequence
def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n -2) + fib2(n - 1) # recursive case

if __name__ == "__main__":
    print(fib2(5)) #15 recursive calls
    print(fib2(10))  #177 recursive calls
    print(fib2(20)) # 21,891 recursive calls
    # print(fib2(50)) # too many recursive calls to finish
# Still this function is limited as every call to fib2() results in two more calls to fib2() 