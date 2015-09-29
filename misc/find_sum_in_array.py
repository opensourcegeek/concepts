

def test_fn():
    given = [5, 2, 6, 3, 4]
    given_sum = 7

    answer = fn(given, given_sum)
    print(answer)
    assert answer == [ [5, 2], [3, 4] ]

    given = [5, 2, 5, 3, 4]
    given_sum = 7

    answer = fn(given, given_sum)
    assert answer == [ [5, 2], [3, 4] ]

    given = [12,2,3,4,1,23,9,8]
    given_sum = 17
    answer = fn(given, given_sum)
    assert answer == [ [12, 2, 3], [9, 8] ]

    given = [3,2,4]
    given_sum = 6
    answer = fn(given, given_sum)
    assert answer == [ [2, 4] ]





def fn(given, given_sum):
    results = []
    sum_ = 0
    result = []

    for i in given:
        sum_ += i
        print "The i is {}".format(i)
        result.append(i)
        print "Sum is {}".format(sum_)
        print "Result current ", result

        while (sum_ > given_sum):
            print("Modifying sub-array")
            elem = result.pop(0)
            sum_ -= elem

        if sum_ == given_sum:
            print "Results are ", results

            results.append(result)
            print(i)
            sum_ = 0
            result = []
            print "Results are ", results

    return results


test_fn()
