def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    def calculate(x, y, operator):
        return int(x) + int(y) if operator == '+' else int(x) - int(y)
    
    def format_problem(num1, num2, operator, width):
        top = num1.rjust(width)
        bottom = operator + num2.rjust(width - 1)
        dash = '-' * width
        return top, bottom, dash

    top_numbers = []
    mid_numbers = []
    dashes = []
    answers = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        # Validation
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the required width (2 spaces plus the longer number)
        width = max(len(num1), len(num2)) + 2

        # Format the problem and append the strings
        top, bottom, dash = format_problem(num1, num2, operator, width)
        top_numbers.append(top)
        mid_numbers.append(bottom)
        dashes.append(dash)
        
        # Calculate the result if show_answers is True
        if show_answers:
            result = str(calculate(num1, num2, operator))
            answers.append(result.rjust(width))

    # Join the formatted problems into final strings
    arranged_problems = '    '.join(top_numbers) + '\n' + '    '.join(mid_numbers) + '\n' + '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems
