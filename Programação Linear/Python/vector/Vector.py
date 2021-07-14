from typing import Any

class VectorComponent:

    def __init__(self, index, number) -> None:

        """
            An auxiliary class, creates an attribute that is passed as a component of a vector of the Vector class.
        """

        try:
            if not isinstance(index, int):
                raise TypeError("Component creation error: the VectorComponent.index attribute must be an int()\n       In: self.index = index\n       index is a %s" % type(index))
            else:
                self.index = index
        except TypeError as err:
            print(err)
            exit()
        try:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("Component creation error: the VectorComponent.number attribute must be an int() or float()\n       In: self.number = number\n       number is a %s" % type(number))
            else:
                self.number = number
        except TypeError as err:
            print(err)
            exit()

class Vector:

    def __init__(self) -> None:
        self.__vector = dict()

    def add(self, component):
        try:
            if not isinstance(component, VectorComponent):
                raise TypeError
            else:
                self.__vector[component.index] = component.number
        except TypeError:
            pass
    
    def vector(self) -> dict:
        """
            Returns the vector, in a dictionary {index: value}
        """
        return self.__vector
    
    def indexes(self) -> tuple:
        """
            Returns a tuple with all vector indexes
        """
        return tuple(self.__vector.keys())
    
    def numbers(self) -> tuple:
        """
            Returns a tuple with all vector values
        """
        return tuple(self.__vector.values())
    
    def component(self, index) -> Any or None:
        """
            Returns the value corresponding to the index, or None if it does not exist
        """
        return self.__vector[index] if index in self.__vector else None
    
    def restriction(self, vectorPart) -> tuple:
        """
            Returns a vectors values. If vectorPart is a part of vector.indexes then x[vectorPart]
            denotes the restriction of x to vectorPart, that is, the vector whose component
            q is vector[q] for each q in vectorPart
        """
        return tuple(filter(lambda c: c is not None, [self.component(q) for q in vectorPart]))
