def calcuate_cost(input_arr):
    diff_value = []
    common_value = 2
    cost = 0
    max_diff = 0
    cost_2 = 0
    for i in input_arr:
        mod_value = i % 3
        if mod_value == 0:
            diff_value.append(mod_value)
            common_value = 0
            cost_2 += 1
        else:
            diff = 3 - mod_value
            diff_value.append(diff)
            cost += diff
            if diff > max_diff:
                max_diff = diff
            if diff < common_value:
                common_value = diff
    total_cost = cost - (common_value * 3) + common_value

    if cost_2 == 3 or (cost_2 == 2 and max_diff == 2):
        total_cost_2 = 1
    else:
        total_cost_2 = cost_2
    print(total_cost)
    print(total_cost_2)

calcuate_cost([1, 3, 3])
