
Background:

In the city of Gridville, urban planners use a digital grid to model urban areas where each cell represents a potential building site. The grid is represented by an n x n binary matrix where 1 indicates an existing building and 0 indicates an empty plot. Planners are considering developing one empty plot to enhance urban connectivity.
Problem Description:

You are given an n x n binary matrix representing Gridville. You are allowed to change at most one 0 to a 1, symbolizing the construction of a new building on an empty plot. Determine the size of the largest possible contiguous urban area (island of 1s) in the grid after applying this operation. An urban area (island) is defined as a group of connected buildings (1s), where connectivity is established horizontally and vertically (not diagonally).
Input:

    The first line contains an integer n, the size of the grid (1 ≤ n ≤ 50).
    This is followed by n lines each containing n characters ('0' or '1'), representing the rows of the grid.

Output:

    Output a single integer, the size of the largest urban area (island of 1s) that can be achieved by changing at most one 0 to a 1.