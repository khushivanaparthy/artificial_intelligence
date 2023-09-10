from collections import deque

# Define the initial and goal state
initial_state = (3, 3, 1)  # (M, C, B)
goal_state = (0, 0, 0)

# Define the possible moves
moves = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]

# Define the breadth-first search algorithm
def bfs():
    # Initialize the queue
    queue = deque()
    queue.append((initial_state, []))
    
    # Initialize the visited set
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if the current state is the goal state
        if current_state == goal_state:
            return path
        
        # Add the current state to the visited set
        visited.add(current_state)
        
        # Generate the next possible states
        m, c, b = current_state
        for move in moves:
            if b == 1:
                next_state = (m - move[0], c - move[1], 0)
            else:
                next_state = (m + move[0], c + move[1], 1)
            
            # Check if the next state is valid
            if is_valid_state(next_state) and next_state not in visited:
                queue.append((next_state, path + [next_state]))
        
    return None

# Define the function to check if a state is valid
def is_valid_state(state):
    m, c, b = state
    
    # Check if the number of missionaries is negative or greater than 3
    if m < 0 or m > 3:
        return False
    
    # Check if the number of cannibals is negative or greater than 3
    if c < 0 or c > 3:
        return False
    
    # Check if the number of cannibals is greater than the number of missionaries on either side
    if (m > 0 and c > m) or (m < 3 and c < m):
        return False
    
    return True

# Solve the Missionaries and Cannibals problem using BFS
solution = bfs()

if solution:
    print("Solution found!")
    for state in solution:
        print(state)
else:
    print("No solution found.")
