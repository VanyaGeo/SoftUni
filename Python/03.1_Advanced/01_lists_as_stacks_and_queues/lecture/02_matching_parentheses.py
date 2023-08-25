algebraic_expression = input()
stack_parentheses = []

for el in range(len(algebraic_expression)):
    if algebraic_expression[el] == "(":
        stack_parentheses.append(el)
    elif algebraic_expression[el] == ")":
        opening_parentheses = stack_parentheses.pop()
        closing_parentheses = el + 1
        print(algebraic_expression[opening_parentheses:closing_parentheses])

