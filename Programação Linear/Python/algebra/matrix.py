class MatrixComponent:

    def __init__(self, row, col, number) -> None:
        try:
            if not isinstance(row, int) and not isinstance(col, int):
                raise TypeError("The row and col attributes must be of type int()")
            else:
                self.row = row
                self.col = col
        except TypeError as err:
            print(err)
            exit()
        try:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("The number attribute must be of type int() or float()")
            else:
                self.number = number
        except TypeError as err:
            print(err)
            exit()

class Matrix:

    def __init__(self) -> None:
        self.__matrix = dict()
    
    def add(self, component) -> None:
        """
            Adds a component to the array. The parameter must be an instance of MatrixComponent()
        """
        try:
            if not isinstance(component, MatrixComponent):
                raise TypeError
            else:
                if not component.row in self.__matrix: 
                    self.__matrix[component.row] = dict()
                self.__matrix[component.row][component.col] = component.number

        except TypeError:
            pass
    
    def change(self, row, col, number) -> None:
        """
            Change the value of matrix[row][col] if row and col 
            are part of the set of row indices and column indices, respectively.
        """
        if row in self.__matrix:
            if col in self.__matrix[row]:
                self.__matrix[row][col] = number

    def matrix(self) -> dict:
        """
            Returns the matrix in a dict {row: {col: number}}
        """
        return self.__matrix
    
    def component(self, row, col):
        """
            Returns the matrix[row][col] number if row and col 
            are part of the set of row indices and column indices, respectively.
        """
        if row in self.__matrix:
            if col in self.__matrix[row]:
                return self.__matrix[row][col]
        return None