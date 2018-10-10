# tetriling_puzzle_code
Challenge set by tutors, they provided 'utils.py' and 'performace_test_v2.py' with functions to generate the grid, test and display the given solution etc.
My solution is 'main.py', it utilises a named-node tree format to store possible Tetris shapes to test against the grid.

It does this through a 'Node' class, where each node's name is it's relative position to the selected square.
The algorithm then uses recursion to iterate through the tree, using the node's name to test if that position fits into the grid. If it does, it calls itself again, so moves onto that child's children in the tree and repeats.
Once it gets to the last child, it returns the name of that piece, as desribed in utils.py.
The process repeats for all available squares in the target grid, if not piece is found to fit, it moves onto the next square.

Using a tree format and recursion drastically reduces running time and by pikcing the most common child each time, it doesn't sacrifice on accuracy.

For a Target Grid of 100 x 100 squares with Density = 0.8: Average Running Time = 0.014 seconds, Average Accuracy = 95.5%.
