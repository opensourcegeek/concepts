def perms(word):
    stack = list(word)
    results = [stack.pop()]

    print("Initial stack ", stack)
    print("Initial results ", results)

    while len(stack) != 0:
        c = stack.pop()
        print("Current ", c)
        print("Results ", results)
        new_results = []
        for w in results:
            print("W ", w)
            for i in range(len(w)+1):
                print("I ", i)
                print("W-inner ", w)
                print("Perm ", w[:i] + c + w[i:])
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results


print(perms('abc'))
