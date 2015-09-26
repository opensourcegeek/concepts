

def test_fn():
    given = [100, 78, 49, 66, 55, 21, 33]

    assert fn(given) == [21, 33, 49, 55, 66, 78, 100]


def fn(given):
    for pass_ in list(xrange(len(given) - 1, 0, -1)):
        print("In pass {}".format(pass_))
        for i in range(pass_):
            print("    {}".format(i))
            if given[i] > given[i + 1]:
                given[i + 1], given[i] = given[i], given[i + 1]
                print(given)
    return given

test_fn()
