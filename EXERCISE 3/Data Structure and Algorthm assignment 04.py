# Example 1: Canvas Actions Stack

# Stack implementation using Python list
canvas_stack = []

# Push actions onto the stack (like stacking books)
canvas_stack.append("Login")         # First action
canvas_stack.append("Open Module")   # Second action
canvas_stack.append("Start Quiz")    # Third action

# Pop one action (undo the last action)
undone_action = canvas_stack.pop()

# Screenshot-style output
print("Stack after pushes: ['Login', 'Open Module', 'Start Quiz']")
print(f"Action undone (popped): {undone_action}")
print(f"Stack now: {canvas_stack}")

# Example 2: UR Student Stack

# Stack implementation using Python list
student_stack = []

# Push tasks onto the stack
student_stack.append("Assignment")
student_stack.append("Presentation")
student_stack.append("Exam Prep")

# Pop two tasks (remove the last two added)
student_stack.pop()  # Removes "Exam Prep"
student_stack.pop()  # Removes "Presentation"

# Screenshot-style output
print("Stack after pushes: ['Assignment', 'Presentation', 'Exam Prep']")
print("After popping two tasks...")
print(f"Stack now: {student_stack}")

# Example 3: UR Faculty Stack
# Challenge: Reverse a list using a stack

original_list = ["One", "Two", "Three", "Four"]
stack = []

# Step 1: Push all items onto the stack
for item in original_list:
    stack.append(item)  # Each append puts the item on top of the stack

# Step 2: Pop all items from the stack to get them in reverse order
reversed_list = []
while stack:
    reversed_list.append(stack.pop())  # Pop removes the top item

# Screenshot-style output
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")
