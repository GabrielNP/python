from timeit import timeit
from random import randint

SAMPLE_SIZE = 100

option_1_times = []
option_2_times = []
option_3_times = []

def time_option_1(x,y,L,R):
    t = timeit(f"{L} < {x} ** {y} <= {R}")
    option_1_times.append(t)

def time_option_2(x,y,L,R):
    t = timeit(f"{x} ** {y} > {L} and {x} ** {y} <= {R}")
    option_2_times.append(t)

def time_option_3(x, y, L, R):
    t = timeit(f"{x} ** {y} in range({L} + 1 , {R} + 1)")
    option_3_times.append(t)

for n in range(SAMPLE_SIZE):
    print("Iteracao: {}".format(n))
    x = randint(1, 100)
    y = randint(1, 100)
    L = randint(1, 100)
    R = randint(1, 100)

    time_option_1(x, y, L, R)
    time_option_2(x, y, L, R)
    time_option_3(x, y, L, R)

print(f"Average of time for Option 1: {sum(option_1_times)/len(option_1_times)}")
print(f"Average of time for Option 2: {sum(option_2_times)/len(option_2_times)}")
print(f"Average of time for Option 3: {sum(option_3_times)/len(option_3_times)}")
