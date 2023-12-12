def smol_factor(n):
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n  # n is a prime number

def A_primes(start, end):
    primes = [num for num in range(start, end + 1) if smol_factor(num) == num]
    return primes

# Main program
while True:
    print("Choose an operation:")
    print("1. Find the smallest factor of a number")
    print("2. Find prime numbers in a range")
    print("0. Terminate")

    choice = int(input("Enter your choice:\n"))

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        num = int(input("Enter a number to find its smallest factor:\n"))
        factor = smol_factor(num)
        print(f"The smallest factor of {num} is: {factor}")
    elif choice == 2:
        start = int(input("Enter a number [start]:\n"))
        end = int(input("Enter a number [end]:\n"))

        primes = A_primes(start, end)

        print(f"Prime numbers between {start} and {end} are: {' '.join(map(str, primes))}")
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")