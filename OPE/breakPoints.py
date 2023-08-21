def breakPoints(c, P):
    P.sort()  # Sorting the petrol pumps in ascending order of distance
    stops = 0
    fuel_left = c
    
    for i in range(1, len(P)):
        distance_to_next_pump = P[i] - P[i-1]

        # If the distance to the next pump is greater than the tank capacity, it's not possible to reach the destination
        if distance_to_next_pump > c:
            return -1
        
        # If the distance to the next pump is greater than the fuel left, make a stop
        if distance_to_next_pump > fuel_left:
            stops += 1
            fuel_left = c  # Refill the tank

        # Subtract the distance to the next pump from the fuel left
        fuel_left -= distance_to_next_pump

    return stops

# Sample input 1
print(breakPoints(50, [0,10,80,100,260,250,230,220,120,140,180,30,40,20,300]))  # Output: 7

# Sample input 2
print(breakPoints(50, [0,51,100,140]))  # Output: -1
