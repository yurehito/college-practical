# Question 37:
# Create a class "Matrix" to represent a matrix.
# Implement operations for addition, subtraction, and multiplication
# rows : number of rows
# cols : number of columns
# matrix : 2D list
# getdata() : to read matrix elements
# dispdata() : to display matrix
# add(m1, m2) : to add two matrices
# subtract(m1, m2) : to subtract two matrices
# multiply(m1, m2) : to multiply two matrices
# Write a main program.

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def getdata(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = float(input(f"Enter element [{i}][{j}]: "))
    
    def dispdata(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end=" ")
            print()
    
    def add(self, m):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
        return result
    
    def subtract(self, m):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
        return result
    
    def multiply(self, m):
        result = Matrix(self.rows, m.cols)
        for i in range(self.rows):
            for j in range(m.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * m.matrix[k][j]
        return result

# Main program
m1 = Matrix(2, 2)
m2 = Matrix(2, 2)
print("Enter first matrix:")
m1.getdata()
print("Enter second matrix:")
m2.getdata()

print("Addition:")
m_add = m1.add(m2)
m_add.dispdata()

print("Subtraction:")
m_sub = m1.subtract(m2)
m_sub.dispdata()
