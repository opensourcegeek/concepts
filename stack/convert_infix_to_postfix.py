from stack import Stack

def test_fn():
    given_expression = 'A + B * C'
    assert fn(given_expression) == 'A B C * +'

    given_expression = 'A + B + C + D'
    assert fn(given_expression) == 'A B + C + D +'

    given_expression = 'A * B + C * D'
    assert fn(given_expression) == 'A B * C D * +'


def fn(infix_expression):
    operators = Stack()
    operands = []
    operator_precedence = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }
    tokens = infix_expression.split()
    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            operands.append(token)

        else:
            if operators.is_empty():
                operators.push(token)

            else:
                curr_item_peek = operators.peek()
                if(operator_precedence[curr_item_peek] >= operator_precedence[token]):
                    item_in_stack = operators.pop()
                    operands.append(item_in_stack)
                    operators.push(token)

                else:
                    operators.push(token)

    print operators.items
    while not operators.is_empty():
        operands.append(operators.pop())

    postfix_expression = ' '.join(operands)
    print(postfix_expression)
    return postfix_expression


test_fn()

