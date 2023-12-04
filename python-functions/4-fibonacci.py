def fibonacci_sequence(n):
    fibonacci_list = [0, 1] #initializing the sequence
    while len(fibonacci_list) < n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    return(fibonacci_list[:n])

