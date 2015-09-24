

def test_fn():
    given_coins_list = [1, 2, 5, 10, 20, 50]
    given_change = 63

    answer = fn(given_coins_list, given_change)
    print answer
    assert answer == [50, 10, 2, 1]
    given_coins_list = [1, 5, 10, 20, 50]
    given_change = 63

    answer = fn(given_coins_list, given_change)
    print answer
    assert answer == [50, 10, 1, 1, 1]
    given_coins_list = [1, 5, 10, 20, 50]
    given_change = 42

    answer = fn(given_coins_list, given_change)
    print answer
    assert answer == [20, 20, 1, 1]




def fn(coins_list, change):
    coins_list.sort()
    coins_list.reverse()
    sum_so_far = 0
    final_coins = []

    for coin in coins_list:
        if coin + sum_so_far > change:
            continue

        else:
            sum_so_far, number_of_same_coin = keep_picking(coin, sum_so_far, change)
            for c in number_of_same_coin:
                final_coins.append(c)
    return final_coins

def keep_picking(coin, sum_so_far, change):
    number_of_same_coin = []
    while (coin + sum_so_far) <= change:
        number_of_same_coin.append(coin)
        sum_so_far += coin
    return (sum_so_far, number_of_same_coin)

test_fn()






