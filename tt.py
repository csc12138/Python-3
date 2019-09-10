def maxCoin(x, num_init):
    """
    :type x: int, requested total money in cents
    :type num_init: list of int, number of each coin
    :rtype: List[int]
    """
    # check input condition
    if (100 * x % 5) != 0:
        print("Cannot pay in exact.")
        return []

    for item in range(len(num_init)):
        if num_init[item] < 0:
            print("Number of coin should be non-negative.")
            return []

    # initialize
    v = [5//5, 10//5, 20//5, 50//5, 100//5]  # normalized value of every coin(cents)
    S = int(100 * x / 5)  # normalized requested value
    coin_init = num_init[::-1]
    N = [list(coin_init) for value in range(S+1)]  # reserved for: number of used coins

    max_coin = [-1] * (S+1)  # reserved for: max number of all used coins; -1 is not achievable
    max_coin[0] = 0
    num_coin = [0] * len(v)  # reserved for: number of used coins

    # dynamic calculate
    for i in range(1, S+1):
        for j in range(len(v)):

            if i < v[j]:  # current total money < coin value
                continue

            else:
                if max_coin[i] < max_coin[i - v[j]] + 1 and max_coin[i - v[j]] + 1 > 0:  # from previous result
                    if N[i - v[j]][j] > 0:  # coin enough
                        max_coin[i] = max_coin[i - v[j]] + 1  # num of coin used: add 1 more coin
                        N[i][j] = N[i - v[j]][j] - 1  # num of coin left: minus 1 coin
                        for k in range(len(v)):
                            if j != k:
                                N[i][k] = N[i - v[j]][k]  # update from previous data

    if max_coin[S] < 0:
        print("Cannot pay in exact or no enough coins.")
        return []

    # return result from used coins
    for q in range(len(v)):
        num_coin[q] = coin_init[q] - N[S][q]
    num_result = list(num_coin[::-1])
    return num_result


if __name__ == '__main__':
    # input total value
    X = float(input("Please enter total amount of money requested by the auntie: "))

    # input number of each coin denomination
    coin_num = []
    coin_val = ["1-dollar", "50-cents", "20-cents", "10-cents", "5-cents"]
    for p in range(5):
        print("Number of " + coin_val[p] + " coins:")
        ele = int(input("Enter: "))
        coin_num.append(ele)

    # main function
    n = maxCoin(X, coin_num)
    print(n)
