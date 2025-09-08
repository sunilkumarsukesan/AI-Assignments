prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

"""
a) Extract the middle five primes: Create a new list containing the five primes in the middle
of the original list
"""
middleFive = prime_numbers[3:8]
print(middleFive)

"""
b) Get every second prime: Create a new list containing every second number from the
original list, starting from the beginning.
"""
everySecondPrime = prime_numbers[0::2]
print(everySecondPrime)

#c) Use negative indexing: Create a new list containing the last three primes of the list.
lastThree = prime_numbers[-3:]
print(lastThree)

#d) Reverse the list: Create a new list that contains all the elements of the original list in reverse order
reverse = prime_numbers[::-1]
print(reverse)

#e) Descending Order: Sort the list in descending order and store it in a new list.
descending = sorted(prime_numbers, reverse=True)
print(descending)
