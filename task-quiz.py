def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        question_data = file.read().split('\n\n')
        for data in question_data:
            question_lines = data.split('\n')
            question = question_lines[0]
            choices = question_lines[1:-1]
            correct_answer = question_lines[-1].split(": ")[1]
            questions.append((question, choices, correct_answer))
    return questions

def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(chr(64 + i) + ') ' + choice)
    user_answer = input('Your answer (A/B/C/D): ').upper()
    return user_answer

def run_quiz(questions):
    score = 0
    for i, (question, choices, correct_answer) in enumerate(questions, 1):
        user_answer = display_question(question, choices)
        if user_answer == correct_answer:
            score += 1
            print('Correct! Your score:', score)
        else:
            print(f'Wrong! The correct answer was {correct_answer}. Your score:', score)
    print('Quiz completed. Your final score is:', score)

if __name__ == '__main':
    quiz_filename = 'quiz.txt'
    questions = load_questions(quiz_filename)
    run_quiz(questions)
