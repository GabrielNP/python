"""
Dynamically call some functions that have a certain pattern and conditions match
"""

class Main(object):
    def __init__(self, attr_a=None, attr_b=None):
        self._attr_a = attr_a
        self._attr_b = attr_b

    def __is_subclass_a(self):
        if True:
            return 'SubclassA'
        return False

    def __is_subclass_b(self):
        return False

    def __is_subclass_c(self):
        return False
    
    def __infer_type(self) -> str:
        for inferred_type in dir(self):
            if inferred_type.startswith('_Parser__is_') != False:
                o_infer = getattr(self, inferred_type)()
                if o_infer != False:
                    return o_infer

    def parse(self) -> dict:
        try:        
            class_name = globals()[self.__infer_type()](self._attr_a, self._attr_b)
            return class_name.parse()
        except:
            return dict()

class SubclassA:
    def __init__(self, attr_a, attr_b):
        self._attr_a = attr_a
        self._attr_b = attr_b

    def parse(self) -> dict:
        return {'a': self._attr_a, 'b': self._attr_b}
        

class SubclassB:
    def parse(self) -> dict:
        pass

class SubclassC:
    def parse(self) -> dict:
        pass

print(Main().parse())
