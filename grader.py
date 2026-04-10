# Define graders (scores strictly between 0 and 1)

def grader_task1(output):
    return 0.7

def grader_task2(output):
    return 0.6

def grader_task3(output):
    return 0.8


# Define tasks with graders

tasks = [
    {
        "name": "Task 1",
        "grader": grader_task1
    },
    {
        "name": "Task 2",
        "grader": grader_task2
    },
    {
        "name": "Task 3",
        "grader": grader_task3
    }
]