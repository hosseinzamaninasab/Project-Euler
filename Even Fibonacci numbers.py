sum_of_even_fibonacci = 0
a, b = 0, 1
while a < 4*10**6:  # put an small number to sure the accuracy
    a, b = b, b+a  # each sequence, first and second number will be second number and sum of previous first and
    # second number
    # print(a)  # make sure that work's fine!
    if a % 2 == 0:
        # print(a)  # make sure we find the right number
        sum_of_even_fibonacci += a
        # print(sum_of_even_fibonacci)  # make sure again
print(sum_of_even_fibonacci)
