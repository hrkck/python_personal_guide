# To Workout with the algorithms of Babbage's Difference Machine, we have to have squares of first two natural numbers already.
# So, they are defines below:

###
integers = [0, 1, 2]
sq_of_integers = [0, 1, 4]
first_differences = [1, 3]
second_differences = [2]
####

# It is said that, to find out square of 47 for example, step by step, we
# have to find squares of all numbers before 47. That means, if you found
# the square of 47, that means, you already know the squares before 47.

for i in range(3):
    requested_square = int(input("enter a number to be squared:"))
    if requested_square <= integers[-1]:
        print("it is already known, sir")

# The rest of the code is about the algorithm of Difference Machine. The
# general stucture lets the computer to compute the square process,
# without even doing a single multiplying...

    else:
        for i in range(requested_square - integers[-1]):
            integers.append(integers[-1] + 1)
            sq_of_integers.append(
                second_differences[-1] + first_differences[-1] + sq_of_integers[-1])
            first_differences.append(sq_of_integers[-1] - sq_of_integers[-2])
        print(sq_of_integers[-1])
