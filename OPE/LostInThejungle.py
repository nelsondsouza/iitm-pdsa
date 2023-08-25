''' 
Lost in the Jungle

Once upon a time, there was a group of adventurous friends who decided to go on a jungle expedition. 
They were exploring the dense, uncharted jungles of “Mystica’. While enjoying their journey, they realized they had lost their way back to the camp.
The jungle was like a maze with various interconnected paths, and the friends had a map that displayed some landmarks and the connections between them. 
Each landmark was represented by a unique integer identifier, and they knew that the connections were bidirectional.

Write a function shortest_path_to_camp(totai_landmarks, connections, current_landmark, camp_landmark) that takes the following parameters:
total_landmarks: An integer n, represents the total number of landmarks in the jungle labelled from 1 to n.
connections: A dictionary which represents the adjacency list of connections, where each key represents the source landmark and values represent the list of adjacent landmarks of the source landmark.
current_landmark: An integer, the current landmark where the friends are currently located.
camp_ landmark: An integer, the landmark of their camp.
The function should return the minimum number of landmarks the friends need to cross to reach their camp (including current landmark and camp landmark).

Sample input
18 #total_landmarks
(1:(2),2211,3,4],3:(2,5],4:(2,6},5: (3,9) ,6:14,7],7: (6,8) ,8: (7,9],9: (5,8],10:18]} #connections
3. #start_landmark
9 #camp_landmark

Sample Output
3 #minimum number of landmarks along the path

Explanation:
The shortest path from landmark 3 to landmark 9 is through the landmarks 3, 5, and 9, with a total of 3 landmarks to cross. Hence, the output is 3.

'''

from collections import deque

def shortest_path_to_camp(total_landmarks, connections, current_landmark, camp_landmark):
    # Creating a visited array to keep track of visited landmarks
    visited = [False] * (total_landmarks + 1)
    # Queue to keep track of the landmarks to visit next
    queue = deque()
    
    # Adding the current landmark to the queue, and mark it as visited
    # Also adding a counter to keep track of the number of landmarks crossed
    queue.append((current_landmark, 1))
    visited[current_landmark] = True
    
    while queue:
        # Dequeue a landmark from the queue
        landmark, count = queue.popleft()
        
        # Check if the landmark is the camp_landmark
        if landmark == camp_landmark:
            return count
        
        # Iterate through the adjacent landmarks of the current landmark
        for neighbor in connections.get(landmark, []):
            # If the adjacent landmark is not visited, mark it as visited and enqueue it
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, count + 1))
                
    # Return -1 if there is no path from current_landmark to camp_landmark
    return -1

# Sample input
total_landmarks = 18
connections = {1:[2,11,3,4],3:[2,5],4:[2,6],5:[3,9],6:[1,4,7],7:[6,8],8:[7,9],9:[5,8],10:[1,8]}
current_landmark = 3
camp_landmark = 9

# Output
print(shortest_path_to_camp(total_landmarks, connections, current_landmark, camp_landmark)) # Output will be 3
