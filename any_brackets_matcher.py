from stack import Stack


def test_fn():
    given_all_braces = '({[]})'
    assert fn(given_all_braces) == True

    given_all_braces = '({[})'
    assert fn(given_all_braces) == False


def fn(given_all_braces):
    s = Stack()
    braces = {
        ')': '(',
        '}': '{',
        ']': '['
    }


    for char in given_all_braces:
        if char in braces.values():
            s.push(char)

        elif char in braces.keys():
            if s.peek() == braces[char]:
                s.pop()

    return s.is_empty()

test_fn()
