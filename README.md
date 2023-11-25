# Path Finding Visualizer 
This project is a visual representation of various pathfinding algorithms. It is built in Python, utilizing the Pygame library for rendering the visual components. The project includes implementations of A*, Dijkstra's, and Breadth-First Search (BFS) algorithms. The visualization enables users to interactively create start and end points and barriers and observe how different algorithms approach pathfinding.

## Algorithms Implemented 

### 1. A* Algorithm

Approach: The A* algorithm searches for the shortest path by combining heuristic-based search with the practicality of Dijkstra's algorithm. The heuristic function used is the Manhattan distance, which estimates the cost of the cheapest path from any node to the goal. A* maintains two scores for each node: the cost to reach the node (g-score) and the estimated cost from the node to the goal (h-score). The f-score, sum of g and h, is minimized to find the shortest path.

Methodology: 
- Implemented the Manhattan distance heuristic to estimate the cost from any node to the goal.
- Used a min-heap priority queue to manage the open set of nodes. This ensures that the node with the lowest f-score (g-score + h-score) is always processed next.
- Maintained a dictionary for each node's g-score (cost from start to node) and f-score (estimated total cost from start to goal through this node).
- Once the goal is reached, the path is reconstructed backward from the goal to the start using a 'came_from' dictionary.

Visualization: Nodes are color-coded to indicate their state: open set (nodes to be explored), closed set (explored nodes), barriers, start, end, and the final path.

### 2. Dijkstra's Algorithm
Approach: This algorithm finds the shortest paths between nodes in a graph. It iteratively visits the nearest unvisited node, updates the distances from the start node to its neighbors, and repeats the process until all nodes are visited. Unlike A*, Dijkstra’s algorithm does not use a heuristic. It uses a simple uniform cost search approach, expanding outwards from the start node and updating the shortest path to each node.

Methodology: 
-  Implemented using a priority queue to always process the next closest node.
- Kept track of the distance from the start node to each node using a dictionary. Nodes are updated with the distance if a shorter path is found.

Visualization: Similar to A*, nodes are colored to represent their status during the search, and the shortest path is highlighted upon completion.

### 3. BFS 
Approach: BFS explores all neighbor nodes at the current depth before moving to the next level. It uses a queue to process nodes in the order they are encountered. BFS is particularly effective in this grid scenario for finding the shortest path when the cost to move from one node to another is the same in all directions.

Methodology:
- Implemented BFS using a queue to explore nodes level by level. This ensures that nodes are visited in the order they are discovered.
- For each node, all unvisited neighbors are added to the queue and marked as visited to prevent reprocessing.
- Similar to A*, a 'came_from' dictionary is used to track the path. Once the end node is found, the path is traced back to the start node.

Visualization: BFS visualizes the level-by-level exploration of nodes, progressively marking nodes visited until the end node is reached.

## Challenges Encountered 
The three main challenges we faced during this challenges were: 
1. Pygame Integration and UI
- Integrating Pygame's event handling without compromising the real-time execution of the algorithms was a complex task. Ensuring a responsive UI during algorithm run-time and user interactions required careful design and testing.
- Facilitating intuitive user interactions for grid customization and reflecting these changes accurately in the algorithm's processing presented challenges, particularly in maintaining state consistency.

2. Path length calculation
- The main challenge we encountered was when integrating the path length calculation into the main code. The code consistently resulted in a value error, which was traced back to incorrect handling of node properties during path reconstruction. The issue stemmed from a misalignment between the path reconstruction logic and the data structure used to store the path. When attempting to calculate the path length, the application encountered nodes with undefined or incorrect values, leading to a value error. The problem was resolved by refining the path reconstruction process, ensuring that each node along the path was correctly accounted for and their properties were accurately tracked.

3. Performance Optimization
- Balancing the algorithms' computational efficiency with the need for clear, understandable visualization was a key concern. The algorithms had to be optimized for speed while still allowing users to track the pathfinding process visually.

## Instructions on Code Execution
- Prerequisites: Ensure Python and Pygame are installed on your system.
- Running the Application: Navigate to the project directory and execute the main Python file, typically main.py.
- Using the Interface:
    - Click to set the start (green) and end (red) points.
    - Drag the cursor to create barriers (black).
    - Select the algorithm:
      - Press 'A' for A*.
      - Press 'D' for Dijkstra's.
      - Press 'B' for BFS.
      - Press the Spacebar to start the visualization.
      - Use 'C' to clear the path. Hold Shift and press 'C' to clear barriers and paths.
     
### Additional Information
- The application displays metrics such as time taken for the algorithm to complete, the number of nodes traversed, and the length of the final path.
- This project serves as an educational tool to understand and compare different pathfinding algorithms in a graphical and interactive way.

### Members 
1. Yunseo Heo
2. Angie Yoedzer


