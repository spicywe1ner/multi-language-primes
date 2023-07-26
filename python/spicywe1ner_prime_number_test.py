import time

test_array = [10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000, 1000000]

for tt in test_array:
    split_time_start = time.monotonic_ns() / 1000000000
    prime_array = [2, 3, 5]
    spacer_array =[2, 3, 5]
    i = 0
    ttt = tt / 2
    while i < ttt: ## Iterator
        spacer_value = spacer_array[-1]
        spacer_value += 2
        j = 0 ## compare length of arrays 
        # print(tt)
        for x in prime_array: ## Prime Checker
            y = spacer_value % x 
            j += 1
            if y == 0:
                break
            elif j == len(prime_array):
                # print("here its stuck")
                prime_array.append(spacer_value)  
        spacer_array.append(spacer_value)
        i += 1
        # print(i)
    split_time_end = time.monotonic_ns() / 1000000000
    split_time = split_time_end - split_time_start
    print("This found", len(prime_array), "primes, in", tt, "numbers in", split_time, "s")
    # print(prime_array)
