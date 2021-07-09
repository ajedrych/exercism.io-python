class Matrix:
    def __init__(self, matrix_string):
        split = matrix_string.split("\n")
        self.matrix = [[int(i) for i in line.split()] for line in split]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.matrix]
        
