
operations_table = {
    '+' : lambda operand1, operand2 : operand1 + operand2,
    '-' : lambda operand1, operand2 : operand1 - operand2,
    '*' : lambda operand1, operand2 : operand1 * operand2,
    '/' : lambda operand1, operand2 : operand1 / operand2
}

operators = ['+', '-', '*', '/']


def evaluate(rpn_expression):
    return evaluate_expression_elements(rpn_expression.split())


def evaluate_expression_elements(elements):
    if len(elements) == 1:
        return int(elements[0])
    elif len(elements) == 3:
        return evaluate_operation_without_nesting(elements)
    else:
        return evaluate_operation_with_nesting(elements)
    

def evaluate_operation_without_nesting(elements):
    operand1 = int(elements[0])
    operand2 = int(elements[1])
    operator = elements[2]

    return operations_table[operator](operand1, operand2)


def evaluate_operation_with_nesting(elements):
    operator_position = find_operator_position(elements)
    
    prefix = elements[0 : operator_position-2]
    elements_for_operation = elements[operator_position-2 : operator_position+1]
    suffix = elements[operator_position+1 :]
    
    new_operation = prefix + [str(evaluate_operation_without_nesting(elements_for_operation))] + suffix
    
    return evaluate_expression_elements(new_operation)


def find_operator_position(elements):
    for i in range(0, len(elements)):
        if elements[i] in operators:
            return i
    return -1