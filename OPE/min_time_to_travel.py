'''
Journey through Indian Railways

India, with its vast and diverse landscape, is connected by an extensive railway network that spans cities, towns, and villages. 
Trains are an integral part of Indian life, providing an affordable and efficient mode of transportation.

You are tasked with writing a program to help travelers to find the shortest time it takes to travel from one city to another using the Indian Railways.

The railway network is represented using an adjacency list where each city is a node, and the connections between cities are represented as directed edges with travel times.

Write a function min_time_to_travel(num_cities, railways_route, start_city, end_city) that takes the following parameters:

num_cities: An integer n, the total number of cities in the railway network (labeled from 1 to n).

railways_route: A dictionary where keys represent the source cities and the values are lists of tuples (destination city, travel_time) 
representing the destination city and travel times from source city to destination city.

start_city: An integer, the starting city.

end_city: An integer, the destination city.

The function should return an integer, the minimum time it takes to travel from the starting city to the destination city using the Indian Railways. If there's no way to reach the destination city trom the starting city, return -1.

Sample Input 1

4 #num_cities

{1: [(2, 3), (3, 5)],2: [(3, 2), (4, 6)],3: [(4, 1)],4: []} #railways_ route

1 #start_city

4 #end_ city

Output

6

Explanation: 
The shortest time to travel from city 1 to city 4 is by taking the path: 1 -> 3 -> 4, with a total travel time of 6.

Sample Input 2

7

{1: [(2, 3), (3, 5)],2: [(3, 2), (4, 6)],3: [(4, 1)],4: [],5: [(6,5),(7,10), (4,12)],6: [(5,5)],7: [(5,15)]}

6

2

Output

-1

Explanation:

City 2 is not reachable from city 6
'''

import heapq

def min_time_to_travel(num_cities, railways_route, start_city, end_city):
    # Create a dictionary to store the minimum travel times to each city
    min_times = {city: float('inf') for city in range(1, num_cities + 1)}
    min_times[start_city] = 0

    # Use a priority queue (min heap) to explore cities in order of minimum travel time
    priority_queue = [(0, start_city)]

    while priority_queue:
        current_time, current_city = heapq.heappop(priority_queue)

        # Check if the current city is the destination city
        if current_city == end_city:
            return current_time

        # Explore neighbors of the current city
        for neighbor, travel_time in railways_route.get(current_city, []):
            new_time = current_time + travel_time

            # If the new time is less than the previously recorded time to reach the neighbor
            if new_time < min_times[neighbor]:
                min_times[neighbor] = new_time
                heapq.heappush(priority_queue, (new_time, neighbor))

    # If the destination city is not reachable from the starting city
    return -1

# Sample Input 1
num_cities1 = 4
railways_route1 = {1: [(2, 3), (3, 5)], 2: [(3, 2), (4, 6)], 3: [(4, 1)], 4: []}
start_city1 = 1
end_city1 = 4

# Sample Input 2
num_cities2 = 7
railways_route2 = {1: [(2, 3), (3, 5)], 2: [(3, 2), (4, 6)], 3: [(4, 1)], 4: [], 5: [(6, 5), (7, 10), (4, 12)], 6: [(5, 5)], 7: [(5, 15)]}
start_city2 = 6
end_city2 = 2

# Output
output1 = min_time_to_travel(num_cities1, railways_route1, start_city1, end_city1)
output2 = min_time_to_travel(num_cities2, railways_route2, start_city2, end_city2)

print("Output 1:", output1)  # Output 1: 6
print("Output 2:", output2)  # Output 2: -1
