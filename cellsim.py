from random import random
class Cell:
    def __init__(self, alive=False):
        '''
        Initialized a dead cell
        '''
        self.alive = alive

    def set_dead(self):
        '''
        set scell state to alive or False
        '''
        self.allive = False

    def set_alive(self):
        '''
        set the cell state to True 
        '''
        self.alive = True

    def __is_alive(self):
        '''
        check if alive
        '''
        return self.alive

    def get_status(self):
        '''
        return cell status
        '''
        if self.alive:
            return 'O'
        return '.'

    def __str__(self):
        '''
        print cell state
        '''
        return self.get_status()

class Cancer(Cell):
    '''
    inherit from cell because cancer is also a cell
    '''
    
    def get_status(self):
        '''
        return cell status
        '''
        if self.alive:
            return 'O'
        return '.'
    
    def update_cell(self, neighbors):
        '''
        update cell status
        '''
        if self.alive:
            if neighbors < 2:
                self.set_dead()
            elif neighbors > 3:
                self.set_dead()
        else:
            if neighbors == 3:
                self.set_alive()

class Tissue:
    def __init__(self , rows=1 , cols=1, CellType=Cell):
        self.CellType = CellType
        self.rows = rows
        self.cols = cols   
        self.matrix = []

        # populate the tissue/matrix
        self.create_tissue()

    # populate tissue with cells    
    def create_tissue(self):
        self.matrix = [[self.CellType() for column_cells in range(self.cols)] for row_cells in range(self.rows)]

    # get cell at matrix[row][col]
    def __getitem__(self, row, col, cell):
        return self.matrix[row][col]

    # update cell at matrix[row][col]
    def __setitem__(self,row, col, cell):
        self.matrix[row][col] = cell


    # update tissue from matrix
    def seed_from_matrix(self, matrix):
        if len(self.matrix) == len(matrix) and len(self.matrix[0]) == len(matrix[0]):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = matrix[i][j]

    # update from file
    def seed_from_file(self, file, cell):
        with open(file, "r") as f:
            fd = [c.strip('\n') for c in f.readlines()]
            # print(fd[0][1])
            
            for i in range(self.rows):
                for j in range(self.cols):
                    if fd[i][j] != self.matrix[i][j].get_status():
                        self.matrix[i][j].alive = not self.matrix[i][j].alive

    def neigbours(self, i, j):# find away to call this from Cell class
            count = 0
            for row in [-1, 0, 1]: 
                if i + row == -1 or i + row == len(self.matrix): # Don't check the upper and lower neighbors if the cell is in in upper / lower boundaries
                    continue
                for col in [-1, 0, 1]:
                    if j + col == -1 or j + col == len(self.matrix[0]) : # Don't check the left and right neighbors if the cell is in left / right boundaries
                        continue
                    if row == 0 and col == 0: # Don't check the index itself
                        continue
                    if self.matrix[i + row][j + col].alive == True :
                        count += 1

            # print(count)
            return count


    # seed random
    def seed_random(self, con, cell):
        self.matrix = [[cell() for column_cells in range(self.cols)] for row_cells in range(self.rows)]
        for row in self.matrix:
            for column in row:
                chance_number = random() < con
                if chance_number:
                    column.set_alive()


    def next_state(self):# try updating in the cell and cancer class
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.neigbours(i, j)
                if self.matrix[i][j].alive == True and (neighbors <= 1 or neighbors >=4):
                    self.matrix[i][j].alive = False
                elif self.matrix[i][j].alive == False and neighbors == 3 :
                    self.matrix[i][j].alive = True
                else:
                    self.matrix[i][j].alive = False




    def __str__(self):
        return '\n'.join(''.join(map(str, [i.get_status() for i in row])) for row in self.matrix)

