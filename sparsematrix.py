class SparseMatrix:
    def __init__(self, rows, cols, elements):
        self.rows = rows # constant time
        self.cols = cols # constant time
        self.elements = elements # O(a), where a is the number of non-zero elements in the matrix
        
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices are not compatible for addition")
            
        result = [] # constant time
        
        i = 0 # constant time
        j = 0 # constant time
        
        # merge-sort-like iteration over non-zero elements of both matrices
        while i < len(self.elements) and j < len(other.elements):
            if self.elements[i][0] == other.elements[j][0] and self.elements[i][1] == other.elements[j][1]:
                # corresponding elements in A and B have the same position, add them
                result.append((self.elements[i][0], self.elements[i][1], self.elements[i][2] + other.elements[j][2]))
                i += 1 # increment i and j
                j += 1
            elif self.elements[i][0] < other.elements[j][0] or (self.elements[i][0] == other.elements[j][0] and self.elements[i][1] < other.elements[j][1]):
                # element in A comes before element in B, add element in A to result
                result.append(self.elements[i])
                i += 1 # increment i
            else:
                # element in B comes before element in A, add element in B to result
                result.append(other.elements[j])
                j += 1 # increment j
                
        # append any remaining elements from A and B to the result
        while i < len(self.elements):
            result.append(self.elements[i])
            i += 1
            
        while j < len(other.elements):
            result.append(other.elements[j])
            j += 1
            
        return SparseMatrix(self.rows, self.cols, result) # O(a + b), where a and b are the number of non-zero elements in A and B
        
