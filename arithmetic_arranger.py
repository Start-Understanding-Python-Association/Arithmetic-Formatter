

def arithmetic_arranger(problems, show_answers=False):
    """Given addition or subtraction problems print them on top of each other.  Optionally
     we can show answers."""
    if len(problems) > 5:
        print('Error: Too many problems.')
    for i in problems:
        if '*' in i or '/' in i:
            print('Error: Operator must be "+" or "-".')
            break
    # Error: Numbers must only contain digits.
    # Error: Numbers cannot be more than four digits.
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''
    for i in problems:
        number_one = ''
        number_two = ''
        sign = ''
        # answer = ''
        switch_to_second_number = False

        for j in i:
            # line_2, line_3, line_4
            if j != ' ' and j != '+' and j != '-' and not switch_to_second_number:
                number_one = number_one + j
                continue
            elif j == '+' or j == '-':
                switch_to_second_number = True
                sign = j
                continue
            elif j != ' ' and switch_to_second_number:
                number_two = number_two + j
                continue

        if len(number_one) > len(number_two):
            width_of_problem = len(number_one) + 2
        else:
            width_of_problem = len(number_two) + 2
        line_1 = line_1 + (width_of_problem - len(number_one)) * ' ' + number_one + '    '
        line_2 = line_2 + sign + (width_of_problem - len(number_two) - 1) * ' ' + number_two + '    '
        line_3 = line_3 + width_of_problem * '-' + '    '
        # if show_answers:
        #     answer = int(number_one) + int(number_two)
        #     line_4 = line_4 + (width_of_problem - len)
    arranged_problems = (line_1, '\n', line_2, '\n', line_3, '\n', line_4)

    return arranged_problems
