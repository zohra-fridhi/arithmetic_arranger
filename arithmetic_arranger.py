"""
This module uses the function arithmetic_arranger to display arithmetic problems
vertically and if wanted with the solution.
"""


def arithmetic_arranger(problems: list[str], calculate_solution: bool = False) -> str:
    spaces_problem: str = " " * 4
    top_row: str = ""
    bottom_row: str = ""
    dashes: str = ""
    results: str = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        active_problem = problem.split()
        first_operand: str = active_problem[0]
        operator: str = active_problem[1]
        second_operand: str = active_problem[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdecimal() and second_operand.isdecimal()):
            return "Error: Numbers must only contain digits."

        if (len(first_operand) and len(second_operand)) > 4:
            return "Error: Numbers cannot be more than four digits."

        length: int = max(len(first_operand), len(second_operand)) + 2
        top_op: str = first_operand.rjust(length)
        bottom_op: str = operator + second_operand.rjust(length - 1)
        separator: str = "-" * length
        result: str = "".rjust(length)

        if calculate_solution:
            if operator == "+":
                result = str(int(first_operand) + int(second_operand)).rjust(length)
            else:
                result = str(int(first_operand) - int(second_operand)).rjust(length)

        if problem == problems[-1]:
            top_row += top_op
            bottom_row += bottom_op
            dashes += separator
            results += result
        else:
            top_row += top_op + spaces_problem
            bottom_row += bottom_op + spaces_problem
            dashes += separator + spaces_problem
            results += result + spaces_problem

    if calculate_solution:
        arranged_problems: str = (
                top_row + "\n" + bottom_row + "\n" + dashes + "\n" + results
        )
    else:
        arranged_problems: str = top_row + "\n" + bottom_row + "\n" + dashes

    return arranged_problems
