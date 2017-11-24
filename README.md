Algorithms to allow a robot to find a path from a source to a destination in a region that contains pre-defined obstacles.

Two algorithms are implemented - **Randomly Exploring Random Forest** (RRT) and **Vertical Cell Decomposition**.

There are two implementations of RRT  - Both use a goal bias of 0.05 and step size of 5.

RRT Result
![RRT](https://raw.githubusercontent.com/shikherneo2/path-planning/master/rrt_naiive.png)

Vertical Cell Decomposition Result
![Vertical Cell Decomposition](https://raw.githubusercontent.com/shikherneo2/path-planning/master/vcd.png)


### Files

***

The helpers folder contains two files - geometry and graph - with helper functions

rrt.py tries to reach the goal after every new vertex is added, and therefore reaches the goal quicker.

rrt_naiive.py keeps expanding the tree till the goal is actually expanded. 

The input file format are as follows
Each line contains end points for a polygon describing an obstacle. The end points are arranged in a counter-clockwise direction.

The final line contains two points - source, and destination.

