

def test_fn():
    given = list(xrange(1, 10000))
    assert fn(given, 9999) == True


def fn(given_array, value):
    mid_item_index = len(given_array) / 2
    current_item = given_array[mid_item_index]
    print(current_item)

    if current_item == value:
        print('Equals')
        return True

    elif current_item > value:
        return fn(given_array[0:mid_item_index], value)

    elif current_item < value:
        return fn(given_array[mid_item_index+1:], value)


test_fn()


