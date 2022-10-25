'''
input: coins = [coins in my possession]

output: minimum amount of change (minimum sum of money) that cannot be created

EXAMPLE
    input
        coins = [1, 2, 5]
    output
        4

ps: if an array is empty, minimum amount of change is 1

SOLUTION

    if coin > change + 1 -> no change

    input
    coins = [1, 2, 5]
        change = 0
        coin = 1
            1 > 0 + 1 ? 
                n
        change = 1
        coin = 2
            2 > 1 + 1 ?
                n
        change = 3
        coin = 5
            5 > 3 + 1
                s
                return change + 1 = 4
'''

def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
      if coin > change + 1:
        return change + 1
      change += coin
    return change + 1
