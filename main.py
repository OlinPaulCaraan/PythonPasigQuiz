# This simple quiz program is made by Olin Paul Caraan

questions = ("1. What is the name of the famous historical house located in Pasig City? ",
                       "2. What river flows through Pasig City? ",
                       "3. Pasig City is part of which region in the Philippines? ",
                       "4. What is the main mode of river transport promoted along the Pasig River? ",
                       "5. Who is the current mayor of Pasig City? ")

options = (("A. Aguinaldo Shrine", "B. Bahay Tsinoy", "C. Bahay na Tisa", "D. Casa Manila"),
                        ("A. Cagayan River", "B. Pasig River", "C. Agno River", "D. Pampanga River"),
                        ("A. Region IV-A", "B. Region III", "C. NCR (National Capital Region)", "D. Region I"),
                        ("A. Jeepney", "B. Bus", "C. Ferry", "D. Train"),
                        ("A. Robert Jaworski Jr.", "B. Bobby Eusebio", "C. Vico Sotto", "D. Iyo Bernardo")
)

answers = ("C", "B", "C", "C", "C")
guesses = []
score = 0
question_num = 0


print("----------------------")
print("  SIMPLENG QUIZ LANG  ")
print(" BY  OLIN PAUL CARAAN ")
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")