from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # our base case 

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n -2) # memoization
    return memo[n]

if __name__ == "__main__":
    print(fib3(50))

# because of memoization we can safely call this new fib fucnction requesting the 50th place fib number
# all previous results are stored in the dictionary so on element 32, previous results for element 31
# are already available unlike fib2.py    