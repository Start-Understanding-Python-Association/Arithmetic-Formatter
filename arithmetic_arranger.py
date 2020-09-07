

def arithmetic_arranger(problems, show_answers=False):
    """Given addition or subtraction problems print them on top of each other.  Optionally
     we can show answers."""
    if len(problems) > 5:
        print('Error: Too many problems.')
    for problem in problems:
        if '*' in problem or '/' in problem:
            print('Error: Operator must be "+" or "-".')
            break
    # Error: Numbers must only contain digits.
    # Error: Numbers cannot be more than four digits.
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''
    for problem in problems:
        number_one = ''
        number_two = ''
        sign = ''
        # answer = ''
        switch_to_second_number = False

        for character in problem:
            if character != ' ' and character != '+' and character != '-' and not switch_to_second_number:
                number_one = number_one + character
                continue
            elif character == '+' or character == '-':
                switch_to_second_number = True
                sign = character
                continue
            elif character != ' ' and switch_to_second_number:
                number_two = number_two + character
                continue

        if len(number_one) > len(number_two):  # take the greater of the lengths of the two numbers and add 2
            width_of_problem = len(number_one) + 2
        else:
            width_of_problem = len(number_two) + 2
        line_1 = line_1 + (width_of_problem - len(number_one)) * ' ' + number_one + '    '
        line_2 = line_2 + sign + (width_of_problem - len(number_two) - 1) * ' ' + number_two + '    '
        line_3 = line_3 + width_of_problem * '-' + '    '
        # if show_answers:
        #     answer = int(number_one) + int(number_two)
        #     line_4 = line_4 + (width_of_problem - len
    line_1 = line_1[:-4]  # take back the 4 extra spaces at the end of each line
    line_2 = line_2[:-4]
    line_3 = line_3[:-4]
    # line_4 = line_4[:-4])
    arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3
    if show_answers:
        arranged_problems = arranged_problems + '\n' + line_4
    return arranged_problems
