# Grade Analyzer

A simple Python program that analyzes student grades, applies a curve, and determines which students pass before and after the curve.

---

## Description

This program works with a list of student names and their corresponding grades. It analyzes the data to determine which students pass based on a minimum grade requirement. It also applies a curve to the grades and re-evaluates the results.

At the end, the program clearly displays:
- Each student and their original grade
- Students who passed before the curve
- Students who passed after the curve
- A final congratulatory message for students who passed

This project was created while learning Python fundamentals and practicing loops, list indexing, conditionals, and working with multiple lists.

---

## How It Works

1. A list of students and their grades is defined.
2. The program displays all students with their original grades.
3. It checks which students passed based on a minimum grade requirement.
4. A curve is applied to all grades.
5. The program checks again to see who passed after the curve.
6. Results are displayed in the terminal.
7. A final message lists all students who passed after the curve.

---

## Example
```text
---- TEST RESULTS ----

Ethan Walker : 98
Olivia Martinez : 96
...

---- Students who passed BEFORE the curve ----

['Ethan Walker', 'Olivia Martinez', ...]

---- Students who passed AFTER the curve ----

['Ethan Walker', 'Olivia Martinez', ...]

---- Big Congratulations to these students! You passed! ----

Ethan Walker
Olivia Martinez
...

---

## Requirements Checked

A student is considered passing if they meet the following:

- Score is greater than or equal to 75

---

## Concepts Used

- Python lists
- Looping with `for`
- Index-based iteration using `range(len())`
- Conditional statements (`if`)
- List comprehensions
- Working with multiple related lists
- Basic data processing
- Console output with `print()`

---

## File Structure
```text
Grade-Analyzer/
│
├── grade_analyzer.py
└── README.md

---

## Future Improvements

- Allow user input for grades
- Add average grade calculation
- Add highest and lowest grade tracking
- Implement different curve methods
- Display results in a more formatted table
- Export results to a file

---

## Author

Chase Garner
