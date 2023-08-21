""" 
Minimum Semester
A university offers an online learning program in which there are total n courses labeled from 0 to n - 1. The program is divided into semesters. You can take any number of courses in one semester, but you can take a course only if you have finished taking its prerequisites.
Information about prerequisites is stored in a dictionary prerequisites where prerequisites[i] = [j,k,...] indicates that you must finish all courses in (j,k,...) first if you want to take the course i. You can start with courses that have no prerequisites.
Write a function minimumDuration(n, prerequisites) that returns the minimum number of semester required to finish all courses of the program. If it is impossible to finish all courses due to bad prerequisites allotment, return -1.
Note:- You can use class Queue given in prefix if required.

Example
Consider that prerequisites for 8 courses is {0:[],1:[],2:[5],3:[0],4:[0],5:[1,3],6:[5],7:[1,3,4,6]} in which we can see that course 0 and 1 have no prerequisite, for taking course 2, we have to finish course 5 first, for taking course 3, we have to finish course 0 first and so on.
So we can start with the courses that have no prerequisite, and we can finish all courses in minimum 5 semester in the following order:-
Sem-1 - 0,1
Sem-2 - 3,4
Sem-3 - 5
Sem-4 - 2,6
S Sem-5 - 7

Sample input 1
8
{0:[],1:[],2:[5],3:[0],4:[0],5:[1,3],6:[5],7:[1,3,4,6]}
Output
5

Sample input 2
8
{0:[],1:[],2:[5],3:[0],4:[0],5:[1,2,3],6:[5],7:[1,3,4,6]}
Output
-1
"""

from collections import deque

def minimumDuration(n, prerequisites):
    in_degree = [0] * n
    adj_list = {i: [] for i in range(n)}

    for course, pre_reqs in prerequisites.items():
        in_degree[course] += len(pre_reqs)
        for pre_req in pre_reqs:
            adj_list[pre_req].append(course)

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    semesters = 0

    while queue:
        semesters += 1
        size = len(queue)
        for i in range(size):
            course = queue.popleft()
            for dependent_course in adj_list[course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)

    return semesters if sum(in_degree) == 0 else -1

# Sample input
n = 8
prerequisites = {0:[],1:[],2:[5],3:[0],4:[0],5:[1,3],6:[5],7:[1,3,4,6]}
print(minimumDuration(n, prerequisites))  # Output: 5

prerequisites = {0:[],1:[],2:[5],3:[0],4:[0],5:[1,2,3],6:[5],7:[1,3,4,6]}
print(minimumDuration(n, prerequisites))  # Output: 5
