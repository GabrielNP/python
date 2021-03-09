# See for loop implementation below:

x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)
print(y)

# Now take a look on same loop with List Comprehension
# new_variable = [value_to_add for iterator in iterable condition]

z = [i**2 for i in x]
print(z)

# Exemple with condition: print only odd of x
g = [i for i in x if i%2==1]
print(g)


# Calling a function
# the value_to_add can be a iterated value or the return of a function that is called with iterated value as a arg
def next_year(age):
    return age + 1

ages = [20, 39, 18, 27, 19]
age_next_year = [next_year(idade) for age in ages]
print(age_next_year)