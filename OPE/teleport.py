'''
Teleport
A sequence of n contiguous rooms are numbered from 0 to n-1 and are separated by locked
doors. You do not have the key for any door. Initially you have no coin and are in room 0. Each
room has a door to the next room which requires lock picking. It takes 1 hour to unlock the door
by lock picking, and lock picking a door gets you one coin. Some rooms have an extra special door
which leads to a room number greater than the current room number, which takes zero time but
requires a number of coins equal to the number of rooms skipped (destination room number -
current room number). One can always go to the next room by locking picking. You have to get to
the last room in the least amount of time possible.
Write a function telteport(D) that returns the number of hours required to reach the last room
for a given sequence of rooms. D is the dictionary such that key is the room number and the
corresponding value is the special door destination. If key = value then the room does not have a
special door.
Consider the below example, rooms 0,1,2,4,5,8,9 have no special door, hence one has to go to the
next room by lock picking with one hour spent and one coin earned. Rooms 3,6,7 have special
doors to 5,9,8 with requirements of paying 2 (5-3), 3 (9-6), 1 (8-9) coins respectively.
+-------+-------+-------+-------+-------+-------+
| key   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
+-------+-------+-------+-------+-------+-------+
| value | 0 | 1 | 2 | 5 | 4 | 5 | 9 | 8 | 8 | 9 |
+-------+-------+-------+-------+-------+-------+
'''

def teleport(D):
    n = len(D)
    coins = 0
    hours = 0
    current_room = 0

    while current_room < n - 1:
        # Check if there's a special door and if we have enough coins to use it
        if D[current_room] > current_room + 1 and coins >= (D[current_room] - current_room - 1):
            # Use the special door
            coins -= (D[current_room] - current_room - 1)
            current_room = D[current_room]
        else:
            # Lockpick the next door
            coins += 1
            hours += 1
            current_room += 1

    return hours

# Example usage
D = {0: 0, 1: 1, 2: 2, 3: 5, 4: 4, 5: 5, 6: 9, 7: 8, 8: 8, 9: 9}
print(teleport(D))  # Output: 7
