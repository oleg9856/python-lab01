if __name__ == '__main__':
    # Prompt the user to enter the value of N
    N = int(input("Enter a number N: "))

    # Initialize a variable for the sum
    total_sum = 0

    # Calculate the sum of natural numbers from 1 to N
    for i in range(1, N + 1):
        total_sum += i

    # Print the result
    print(f"The sum of natural numbers from 1 to {N} is {total_sum}")