from stack import Stack


def test_fn():
    given_braces = '((()))'
    assert fn(given_braces) == True

    given_braces = '((())'
    assert fn(given_braces) == False


def fn(given_braces):
    s = Stack()
    open_char = '('
    close_char = ')'

    for char in given_braces:
        if char == open_char:
            s.push(char)

        if char == close_char:
            s.pop()

    return s.is_empty()


test_fn()



