def is_prime(number):
    if number < 2:
        return False  # Numbers less than 2 are not prime

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any other number, it's not prime

    return True  # If the number is not divisible by any other number, it's prime