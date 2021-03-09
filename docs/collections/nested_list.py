import numpy as np

from functools import reduce
from datetime import datetime

"""Sum the subtraction of each element (sublist) of list"""

"""ATTENTION! required to run pip install -r requirements.txt"""

SAMPLE_SIZE = 1000000

class NestedList:

    def __init__(self):
        self.nested_list = [[1,2], [4,5], [8,9]] * SAMPLE_SIZE

    def __time_option_1(self):
        """for + subtraction operation + reduce"""
        start = datetime.now()
        concat_list = list()
        for i in self.nested_list:
            concat_list += [i[1] - i[0]]
        reduce(lambda a,b: a+b, concat_list)
        end = datetime.now()
        return end - start

    def __time_option_2(self):
        """for + double reduce"""
        start = datetime.now()
        concat_list = list()
        for i in self.nested_list: 
            concat_list.append(reduce(lambda a,b: b-a, i))
        reduce(lambda a,b: a+b, concat_list)
        end = datetime.now()
        return end - start

    def __time_option_3(self):
        """double reduce + map"""
        start = datetime.now()
        concat_list = list()
        reduce(lambda a,b: a+b, list(map(lambda i: reduce(lambda a,b: b-a, i), self.nested_list)))
        end = datetime.now()
        return end - start

    def __time_option_4(self):
        """for in numpy array + np sum"""

        start = datetime.now()
        np_array = np.array(self.nested_list)
        it = [np_array[i][1] - np_array[i][0]  for i in range(len(np_array))]
        np.sum(it)
        end = datetime.now()
        return end - start

    def main(self):
        all_function_names = list()
        all_function_values = list()
        for function in dir(self):
            if function.startswith('_NestedList__time_option_'):
                o_nested_list = getattr(self, function)()
                print(o_nested_list)
                all_function_names.append(function)
                all_function_values.append(o_nested_list)

        minor = min([t for t in all_function_values])
        fastest_function = all_function_names[all_function_values.index(minor)]

        print(f"\nThe fastest was {fastest_function} - {minor}s")
                

NestedList().main()
