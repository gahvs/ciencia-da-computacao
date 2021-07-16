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
        self.__rows = list()
        self.__cols = list()
        self.__matrix = dict()
    
    def __fill(self) -> None:
        """
            When a new column is added this method is called. 
            Its function is to fill the other columns with the 
            new component added (and with the number = 0)
        """
        for row in self.__rows:
            for col in self.__cols:
                if not col in self.__matrix[row]:
                    self.__matrix[row][col] = 0

    def add(self, component) -> None:
        """
            Adds a component to the array. The parameter must be an instance of MatrixComponent().
            If the component already exists the method will do nothing.
            To modify a value in the array use the change() method.
        """
        try:
            if not isinstance(component, MatrixComponent):
                raise TypeError
            else:
                if component.row in self.__matrix:
                    if component.col in self.__matrix[component.row]:
                        return # throw error? (component already exists)
                else:
                    self.__matrix[component.row] = dict()
                
                self.__rows.append(component.row)
                self.__cols.append(component.col)
                self.__matrix[component.row][component.col] = component.number
                self.__fill()

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
    
    def restriction(self, rowPart, colPart):
        """
            Returns an array defined over all p and q in rowPart and colPart, respectively.
            When you want the part to be the whole, rowPart or colPart must be ","
        """
        if rowPart == ",": rowPart = self.__rows[:]
        if colPart == ",": colPart = self.__cols[:]
        restriction = Matrix()
        for row in rowPart:
            for col in colPart:
                restriction.add(MatrixComponent(row, col, self.__matrix[row][col]))
        return restriction