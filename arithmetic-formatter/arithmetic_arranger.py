def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i, problem in enumerate(problems):

        operand1, operator, operand2 = problem.split()

        if operator not in {'+', '-'}:
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        line1 += operand1.rjust(width)
        line2 += operator + operand2.rjust(width - 1)
        line3 += '-' * width

        if operator == "+":
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))

        line4 += result.rjust(width)

        if i != len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    return arranged_problems

