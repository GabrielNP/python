"""
Here the basic list usage.
"""

# make a list
list1 = ["abacaxi", "melancia", "abacate"]
list2 = [1, 2, 3, 4, 5]


# concat
list3 = list1 + list2
list4 = list3 + [8.9, False]


# loop
for item in list4:
    print(item)


# len() method: return list length
length = len(list4)


# append() method: add in the end of list
list4.append("limao")

# check if there is some element inside list
if 7 in list4:
    print("7 is on list")
else:
    print("7 is not on list")


# remove() method: remove some specific (and required) element on list
list4.remove("limao")


# del() method: remove some element by its position
del list4[2:]


# declare empty list
list5 = []
list_5 = list()


# list sorting
# sort() method does not return and affects original list
# sorted() method: returns the sorting and does not change original list

list1 = [9,1,5,4,6,8,2]
sorted_list = lista
list1.sort()

print(list1)
print(sorted(sorted_list))

# reverse sorting
list1.sort(reverse=True)
sorted(sorted_list, reverse=True)
list(reversed(sorted(sorted_list)))

# inverse list
list1.reverse()


# count() method: ocurrencies counting
values = [ 0, 0, 1, 2, 0, 3, 4]
values.count(0))


# index method: returns some element's index
fruits = ['Banana', 'Morango', 'Maçã', 'Uva']
fruits.index('Morango'))

searched_fruit = 'Melancia'
if searched_fruit in fruits:
    print(fruits.index(searched_fruit))
else:
    print('Sorry, {} is not on this list.'.format(searched_fruit))


# Array
"""Arrays are for numpy lib."""


# extend method: extend a third list inside a list
list1.extend(list3)