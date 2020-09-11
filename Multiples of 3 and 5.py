sum_multiples = 0  # we should put this outside for loop not inside
for i in range(1, 1000):  # at first set range(1, 10) to see what happens and debugging would be much easier
    # print(i)  # to make sure that our program works fine!
    if i % 3 == 0 or i % 5 == 0:  # check if they are multiples of 3 & 5 or not
        # print(i)  # make sure we got right numbers
        sum_multiples += i  # add i to sum_multiple each time
print(sum_multiples)
