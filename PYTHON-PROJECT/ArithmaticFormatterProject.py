def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = []
    first_numbers = []
    second_numbers = []

    for problem in problems:
        parts = problem.split()
        first_numbers.append(parts[0])
        operators.append(parts[1])
        second_numbers.append(parts[2])

    for operator in operators:
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    for num in first_numbers + second_numbers:
        if not num.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."

    arranged_problems = ""
    answers = []

    for i in range(len(problems)):
        first_num = first_numbers[i]
        second_num = second_numbers[i]
        operator = operators[i]

        num1_width = len(first_num)
        num2_width = len(second_num)
        width = max(num1_width, num2_width) + 2

        arranged_problems += first_num.rjust(width)
        if i < len(problems) - 1:
            arranged_problems += " " * 4

        if operator == '+':
            answers.append(str(int(first_num) + int(second_num)))
        else:
            answers.append(str(int(first_num) - int(second_num)))

    arranged_problems += "\n"

    for i in range(len(problems)):
        second_num = second_numbers[i]
        operator = operators[i]
        num1_width = len(first_numbers[i])
        num2_width = len(second_num)
        width = max(num1_width, num2_width) + 2

        arranged_problems += operator + " " + second_num.rjust(width - 2)
        if i < len(problems) - 1:
            arranged_problems += " " * 4

    arranged_problems += "\n"

    for i in range(len(problems)):
        num1_width = len(first_numbers[i])
        num2_width = len(second_numbers[i])
        width = max(num1_width, num2_width) + 2
        arranged_problems += "-" * width
        if i < len(problems) - 1:
            arranged_problems += " " * 4

    if show_answers:
        arranged_problems += "\n"
        for i in range(len(answers)):
            num1_width = len(first_numbers[i])
            num2_width = len(second_numbers[i])
            width = max(num1_width, num2_width) + 2
            arranged_problems += answers[i].rjust(width)
            if i < len(answers) - 1:
                arranged_problems += " " * 4

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
