def get_combinations(target, coins, current_combination=[], start_index=0):
    if target == 0:
        return [current_combination]
    if target < 0:
        return []
    
    combinations = []
    for i in range(start_index, len(coins)):
        coin = coins[i]
        new_combination = current_combination + [coin]
        combinations += get_combinations(target - coin, coins, new_combination, i)
    return combinations


coins = [1, 5, 10, 25]
target = 40
combinations = get_combinations(target, coins)