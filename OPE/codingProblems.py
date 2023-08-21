"""Coding competition teams

There are n students in the current PDSA term of the IITM Online Degree Phogram. Assume that the number of students is even. The ith student has programming skill denoted by a positive integer ai.

The instructors want to form n/2 teams for an upcoming coding competition. Each team should consist of exactly two students, and each student should belong to exactly one team. Two students can form a team only if their skills are equal (otherwise they cannot understand each other and cannot form a team).

Students can solve problems to increase their skill. One solved problem increases the skill by one.
The instructor wants to know the minimum total number of problems students should solve to form exactly r/2 teams (i.e. each students should be part of a team).

Write a function coding problems{students) that takes as input a list students with indices from 0 to n-1, and the element at index { of list students represents the programming skill of student i. The function returns the minimum total number of problems students should solve to form exactly n/2 teams as output.

Example
Consider the list students to be [5, 10, 2, 3, 14, 5]. In this case, the optimal teams will be (2,3), (0,5), and (1,4), where each pair denotes a team in terms of the indices of the students. Then, to form the first team the third student should solve 1 problem, to form the second team nobody needs to solve problems, and to form the third team the second student should solve 4 problems,
so the answer is 1 + 4 = 5.

Sample input 1
[5,10,2,3,14,5]
Output
5

Sample Input 2
[1,100]
Output
99"""

""" def codingProblems(students):
    n = len(students)
    cnt = 0
    students.sort()
    for i in range(0, n, 2):
        cnt += students[i + 1] - students[i]
    return cnt

students = [5, 10, 2, 3, 14, 5]
print(codingProblems(students))

students = [1, 100]
print(codingProblems(students)) """

def coding_problems(students):
    students.sort() # Sort the skills
    problems_to_solve = 0

    # Iterate through the sorted list by step 2 and sum the differences between adjacent elements
    for i in range(0, len(students), 2):
        problems_to_solve += abs(students[i] - students[i + 1])

    return problems_to_solve

# Sample Input 1
students1 = [5,10,2,3,14,5]
print(coding_problems(students1)) # Output: 5

# Sample Input 2
students2 = [1,100]
print(coding_problems(students2)) # Output: 99
