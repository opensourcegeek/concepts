

def test_fn():
    given = [1, 3, 5, 6, 2, 21, 19, 22]
    answer = fn(given)
    print "Answer is: ", answer
    assert answer == [1, 2, 3, 5, 6, 19, 21, 22]


def fn(array):
    print(array)
    if len(array) < 2:
        return array

    mid = len(array) / 2
    left = array[:mid]
    right = array[mid:]
    fn(left)
    fn(right)

    i = j = k = 0
    print array
    while ((i < len(left)) and (j < len(right))):

        if (left[i] < right[j]):
            array[k] = left[i]
            i += 1

        elif (right[j] < left[i]):
            array[k] = right[j]
            j += 1

        k += 1

    while (i < len(left)):
        array[k] = left.pop()
        k += 1
        i += 1

    while (j < len(right)):
        array[k] = right[j]
        k += 1
        j += 1

    return array



def merge(array, left, right):
    i = j = k = 0
    print array
    while ((i < len(left)) and (j < len(right))):

        if (left[i] < right[j]):
            array[k] = left.pop(i)
            i += 1

        elif (right[j] < left[i]):
            array[k] = right.pop(j)
            j += 1

        k += 1

    while (len(left) > 0):
        array[k] = left.pop()
        k += 1

    while (len(right) > 0):
        array[k] = right.pop()
        k += 1

    return array


test_fn()
