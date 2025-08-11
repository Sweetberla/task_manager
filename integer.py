# Ask user to input their score as a number
score = int(input("what is your score number\n"))
# If score is between 90 to 100 (inclusive) print grade A
if score >= 90 and score <= 100:
    print("grade A")
# If score is between 80 to 89 (inclusive) print grade B
if score >= 80 and score <= 89:
    print("grade B")
# If score is between 70 to 79 (inclusive) print grade C
if score >= 70 and score <= 79:
    print("grade C")
# If score is between 60 to 69 (inclusive) print grade D
if score >= 60 and score <= 69:
    print("grade D")
# If score is between 0 to 59 (inclusive) print grade F
if score >= 0 and score <= 59:
    print("grade F")