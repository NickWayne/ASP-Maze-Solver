# ASP-Maze-Solver
This is an ASP program that solves mazes. It will find the most efficient path and return the results.

# How to run
> `dlv maze.pl maze_solver.pl -filter=inpath`

(inpath is the steps to get to the end)
********************

# Function
The program works by taking all of the open spots, and making them nodes. 
Once these nodes are created, edges are made by finding nodes next to eachother
Now there is disjunction to get all possibilities, using inpath and notpath
Reachable is a recursive rule that finds the path from the root to all paths
Next the sets are constrained to iff they have a reachable from the start to the end
(This is hard coded in for the start and end locations)
then a weak constraint is used to minimize the amount of steps to get to the end
*******************


# Requirements
You can change the maze if you have python 2.7.X installed on your computer
pygame for your version of python 2.7.X.
DLV is included with the files
**********************

# Controls
left click - remove walls (can hold)
right click - add walls (can hold)
space - save the maze to the maze.pl text file
L - load the maze from the maze.pl text file
P - prints out the data in the format of the maze
******************

# Extra info
The maze.pl file is where the data for the maze is stored, and the maze_solver.pl is where the logic is stored.
Because this is brute force, it is very slow and this is just a proof of concept, not to be used for escaping actual mazes

1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 0 0 0 0 0 0 1 0 0 0 0 0 1 1 1 1 1 1 1 
1 1 1 0 1 1 1 1 0 1 1 1 0 0 0 0 0 1 1 1 
1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 1 0 1 1 1 
1 1 1 1 1 0 0 0 1 1 1 0 0 0 0 1 0 0 1 1 
1 0 0 0 1 1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 
1 0 1 0 0 1 1 1 1 0 0 1 1 1 0 1 1 0 1 1 
1 0 1 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 
1 0 1 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 0 1 
1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 
1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 1 
1 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 
1 1 1 0 0 0 1 0 1 1 1 1 1 1 1 1 1 1 0 1 
1 1 0 1 1 1 1 1 1 0 0 0 1 0 0 0 0 0 0 1 
1 0 1 0 0 0 0 1 0 0 1 0 1 0 1 1 1 1 1 1 
1 0 0 1 1 1 0 0 0 1 1 0 1 0 1 1 1 1 1 1 
1 1 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 

This is how the maze is stored, walls are 1's and halls are 0's

Feel free to edit the python code or the ASP code to make it more effiecient or cooler
contact me with any questions or additions made, hope you enjoy :)
********************

BY - Nick Wayne

DATE - 6/15/2017

CONTACT - waynens@miamioh.edu
