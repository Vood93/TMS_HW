def cyclic_sequence(numbers):

    while True:
        for num in numbers:
            yield num


numbers_str = input("Вenter the numbers for the sequence (separated by spaces) :")
numbers_list = [int(num) for num in numbers_str.split()]

n = int(input("Enter the number of items to output:"))

seq_gen = cyclic_sequence(numbers_list)
for _ in range(n):
    print(next(seq_gen), end=" ")
