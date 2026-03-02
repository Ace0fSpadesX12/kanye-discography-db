
#Common Dictionary Stuff

students = {
    "Sean": {"grade": 88, "subject": "Python"},
    "Amy": {"grade": 95, "subject": "Data Science"}
}

students.keys()    # all the keys
students.values()  # all the values      for key, value in students.items():
students.items()   # both, as pairs

for key, value in person.items():
    print(f"{key}: {value}")
#That's a really common pattern in real code. Read it as "for each key-value '
#'pair in the dictionary, give me both."

1. +=, -=, *=, /= (augmented assignment)

Explicit: total = total + n

Shorthand: total += n

Rule: Use shorthand when it naturally reads as an update and doesn’t require extra thinking. 
If you’re still learning, stick to the explicit form—clarity > compactness.

2. List comprehensions vs loops
# Explicit
squares = []
for x in range(5):
    squares.append(x**2)

# Shorthand
squares = [x**2 for x in range(5)]

When it helps: Short list transformations or filters.

When it hurts: Long, nested, or complex logic. If your brain has to pause and unpack it, 
a regular for loop is clearer.

3. Ternary / inline if
# Explicit
if score >= 50:
    result = "pass"
else:
    result = "fail"

# Shorthand
result = "pass" if score >= 50 else "fail"

When it helps: Single simple assignment.

When it hurts: Anything with multiple conditions; the explicit version communicates 
logic more directly.

4. Multiple assignment
# Explicit
a = 1
b = 2
c = 3

# Shorthand
a, b, c = 1, 2, 3

When it helps: Clear grouping of variables; fewer lines.

When it hurts: If it splits related but conceptually different things—your brain 
has to track positions instead of meaning.

5. Boolean shorthand
# Explicit
if is_ready == True:
    start()

# Shorthand
if is_ready:
    start()

When it helps: Common truthy/falsy checks.

When it hurts: Confusing negations like if not is_ready is False:. Now the shorthand 
adds mental gymnastics.


