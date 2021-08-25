
operations_table = {
    '+' : lambda operand1, operand2 : operand1 + operand2,
    '-' : lambda operand1, operand2 : operand1 - operand2,
    '*' : lambda operand1, operand2 : operand1 * operand2,
    '/' : lambda operand1, operand2 : operand1 / operand2
}

operators = ['+', '-', '*', '/']


def evaluate(rpn_expression):
    return __evaluate_expression_elements(rpn_expression.split())


def __evaluate_expression_elements(elements):
    if len(elements) == 1:
        return int(elements[0])
    elif len(elements) == 3:
        return __evaluate_operation_without_nesting(elements)
    else:
        return __evaluate_operation_with_nesting(elements)
    

def __evaluate_operation_without_nesting(elements):
    operand1 = int(elements[0])
    operand2 = int(elements[1])
    operator = elements[2]

    return operations_table[operator](operand1, operand2)


def __evaluate_operation_with_nesting(elements):
    prefix, op_without_nesting, suffix = __split_operation(elements)
    new_operation = prefix + [__evaluate_operation_without_nesting(op_without_nesting)] + suffix
    
    return __evaluate_expression_elements(new_operation)


def __split_operation(elements):
    operator_pos = __find_first_operator_position(elements)
    
    prefix = elements[0 : operator_pos-2]
    operation_without_nesting = elements[operator_pos-2 : operator_pos+1]
    suffix = elements[operator_pos+1 :]

    return (prefix, operation_without_nesting, suffix)


def __find_first_operator_position(elements):
    for i in range(0, len(elements)):
        if elements[i] in operators:
            return i
    return -1