# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN FILE EXAMPLE
# Authors: Liuqing Chen, Feng Shi, 
#          and Isaac Engel (13th September 2017)
# Last updated: 13th September 2017
# ####################################################

# Write or import your functions in this file

from utils import *


def Tetris(target):  # inputs target grid

    global found                                    # global variable for use in recursive function

    class Node:                                     # creates the class 'Node'
        def __init__(self, data, children=None):    # initialising the class
            if children is None:
                children = []
            self.data = data
            self.children = children

        def __str__(self):                          # function to return the node's own data
            return str(self.data)

        __repr__ = __str__

    tree = Node((0, 0), [                     # creating the tree using the above node class
        Node((1, 0), [                        # first child/ square to test if available
            Node((0, 1), [                    # first grandchild/ square to test if the above square is available
                Node((1, 1), [Node(1)]),      # first Great-Grandchild/ final square to test
                Node((2, 0), [Node(10)]),     # second Great-Grandchild/ next square if one above is not available
                Node((1, -1), [Node(16)]),    # etc. etc.
                Node((0, 2), [Node(7)]),
            ]),
            Node((1, 1), [
                Node((2, 0), [Node(12)]),
                Node((1, -1), [Node(13)]),
                Node((1, 2), [Node(11)]),
                Node((2, 1), [Node(17)]),
            ]),
            Node((2, 0), [
                Node((1, -1), [Node(14)]),
                Node((2, 1), [Node(4)]),
                Node((2, -1), [Node(8)]),
                Node((3, 0), [Node(2)]),
            ]),
            Node((1, -1), [
                Node((2, -1), [Node(19)]),
                Node((1, -2), [Node(5)]),
            ]),
        ]),
        Node((0, 1), [
            Node((1, 1), [
                Node((0, 2), [Node(15)]),
                Node((1, 2), [Node(18)]),
                Node((2, 1), [Node(6)]),
            ]),
            Node((0, 2), [
                Node((1, 2), [Node(9)]),
                Node((0, 3), [Node(3)]),
            ])
        ])
    ])

    def get_my_path(x, y, target, solution, node, path=None):    # recursive function to traverse tree and test squares
        global found
        if path is None:                   # initialising path list
            path = []
        path.append(node)                  # add current node to list
        if len(path) < 4:                  # have we found 4 empty squares so we can put a piece in? If not, continue...
            for child in node.children:    # test each child to see if it's position will fit
                j = child.data[0]
                i = child.data[1]
                try:
                    if x + i < 0: raise IndexError    # stops it testing squares outside of target grid
                                                      # is square free in target and solution grid?
                                                      # then the function calls itself recursively
                    if target[y + j][x + i] == 1 and solution[y + j][x + i] == (0, 0):
                        tentative_path = get_my_path(x, y, target, solution, child, path[:])
                        if tentative_path:            # if path/ possible piece exists update path
                            path = tentative_path
                        if found:                     # if found continue to jump out of recursive loops
                            return path
                except IndexError: pass
        else:                                # we've now found 4 empty squares
            found = True                     # change global variable found
            path.append(node.children[0])    # append the last child which is the number of that piece
            return path                      # return/ triggers jump out of the recursive loops

    def fit_shape(x, y, solution, shape_id, pcount):    # function to put found shape into solution grid
        shape = generate_shape(shape_id)                # uses a utils.py function to generate the shape
        for square in range(0, 4):                      # updates solution grid
            j = shape[square][0]
            i = shape[square][1]
            solution[y+j][x+i] = shape_id, pcount
        return solution                                 # returns updated solution grid

    solution = []                                                  # creates a blank list for solution
    for y in (generate_target(len(target), len(target[0]), 0)):    # cycles through each list in an empty target
        b = [(i, 0) for i in y]                                    # makes a tuple for each element
        solution.append(b)                                         # appends this tuple into the solution list of lists

    pcount = 1          # initialise variables for use in main loop
    ycount = 0

    for y in target:    # main loop to find solution, iterates through every square in the grid
        xcount = 0      # initialise count for x column
        for x in y:
            if x == 1 and solution[ycount][xcount] == (0, 0):                # if square is available
                found = False                                                # reset global 'found' variable
                shape = get_my_path(xcount, ycount, target, solution, tree)  # run above function
                if shape:
                    shape_id = int(float(str(shape[-1])))                    # converting shape node name to integer
                    solution = fit_shape(xcount, ycount, solution, shape_id, pcount)    # add shape to solution grid
                    pcount += 1                                              # counter for labeling inputted shapes
            xcount += 1
        ycount += 1

    return solution    # outputs solution grid
