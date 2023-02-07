"""Part One:
Implement a Matrix class that allows for matrix addition and multiplication. 
Make reasonable and appropriate design decisions and justify them in comments or in the discussion board. 
(If addition and multiplication are undefined, then throw an exception.)
You will implement operator overloading so that the '+' and '*' symbols can be used. 
"""

class Matrix:
    def __init__(self, matrix):
        """
        Initializes a Matrix object with a given 2D matrix.
        """
        self.matrix = matrix

    def __str__(self):
        """
        Returns a string representation of the matrix.
        """
        return str(self.matrix)

    def __add__(self, other):
        """
        Implements the '+' operator for matrix addition.
        """
        # Check if matrices have the same dimensions
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise Exception("You can't add matrices with different dimensions!")
        
        result = []
        
        # Loop through each row of the matrices
        for i in range(len(self.matrix)):
            row = []
            
            # Loop through each element in the row
            for j in range(len(self.matrix[0])):
                # Add corresponding elements from both matrices
                row.append(self.matrix[i][j] + other.matrix[i][j])
            
            result.append(row)
        
        return Matrix(result)

    def __mul__(self, other):
        """
        Implements the '*' operator for matrix multiplication.
        """
        # Check if the second operand is a scalar
        if type(other) == int or type(other) == float:
            result = []
            
            # Loop through each row of the matrix
            for i in range(len(self.matrix)):
                row = []
                
                # Loop through each element in the row
                for j in range(len(self.matrix[0])):
                    # Multiply each element by the scalar
                    row.append(self.matrix[i][j] * other)
                
                result.append(row)
            
            return Matrix(result)
        else:
            # Matrix multiplication
            # Check if the number of columns in the first matrix is equal to the number of rows in the second matrix
            if len(self.matrix[0]) != len(other.matrix):
                raise Exception("The dimensions are incompatible with multiplication!")
            
            result = []
            
            # Loop through each row of the first matrix
            for i in range(len(self.matrix)):
                row = []
                
                # Loop through each column of the second matrix
                for j in range(len(other.matrix[0])):
                    element = 0
                    
                    # Loop through each row of the second matrix
                    for k in range(len(other.matrix)):
                        # Calculate the dot product of the corresponding row and column
                        element += self.matrix[i][k] * other.matrix[k][j]
                    
                    row.append(element)
                
                result.append(row)
            
            return Matrix(result)


"""Part Two:
Implement a Vector class that inherets from the Matrix class. 
It will inheret addition and multiplication (inner product) but will also have a 
multiplication method for an outer product (choose an intuitive symbol). 
(If addition and multiplication are undefined due to size mismatch, then throw an exception.)
"""

class Vector(Matrix):
    def __init__(self, vector):
        """
        Initializes a Vector object with a given 1D vector.
        """
        # Call the parent class's constructor with the vector in a single row matrix
        super().__init__([vector])

    def __mul__(self, other):
        """
        Implements the '*' operator for inner product.
        """
        # Check if the second operand is a scalar
        if type(other) == int or type(other) == float:
            result = []
            
            # Loop through each element in the vector
            for i in range(len(self.matrix[0])):
                result.append(self.matrix[0][i] * other)
            
            return Vector(result)
        else:
            # Inner product
            # Check if both vectors have the same number of elements
            if len(self.matrix[0]) != len(other.matrix[0]):
                raise Exception("Inner product undefined for vectors with different number of elements")
            
            result = 0
            
            # Loop through each element in both vectors
            for i in range(len(self.matrix[0])):
                result += self.matrix[0][i] * other.matrix[0][i]
            
            return result

    def outer_product(self, other):
        """
        Implements the outer product between two vectors.
        """
        result = []
        
        # Loop through each element in the first vector
        for i in range(len(self.matrix[0])):
            row = []
            
            # Loop through each element in the second vector
            for j in range(len(other.matrix[0])):
                row.append(self.matrix[0][i] * other.matrix[0][j])
            
            result.append(row)
        
        return Matrix(result)
