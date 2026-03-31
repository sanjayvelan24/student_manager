# Task 2 — file_manager.py
# Create two functions:

# load_students(filename) — reads the JSON file and returns a list. If file doesn't exist, return an empty list []
# save_students(filename, students_list) — writes the list to the JSON file

# Handle the missing file using exception handling.

import json
def load_students(filename):
    try:
        with open(f"{filename}","r")as f:
            return json.load(f)
    except FileNotFoundError as e:
        return []
def save_students(filename, students_list):
    try:
        with open(f"{filename}","w")as f:
            json.dump(students_list,f)
            return "Saved successfully"
    except Exception as e:
        print(f"Error saving file: {e}")
    
# result = load_students("students.json")
# print(result)

# res = save_students("students.json", [{"name": "sanjay", "marks": 45, "grade": "C"}])
# print(res)
