class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


def fractional_knapsack_max_value(wt, val, capacity):
    i_val = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
    i_val.sort(reverse=True)
    solution = []
    total_value = 0
    for i in i_val:
        cur_wt = int(i.wt)
        cur_val = int(i.val)
        if capacity - cur_wt >= 0:
            capacity -= cur_wt
            total_value += cur_val
            solution.append(
                {'item': i, 'total_value': cur_val, 'fraction': 100})
        else:
            fraction = capacity / cur_wt
            total_value += cur_val * fraction
            capacity = int(capacity - (cur_wt * fraction))
            solution.append(
                {'item': i, 'total_value': cur_val * fraction, 'fraction': fraction})
            break
    return total_value, solution


def print_solution(solution):
    for i in solution:
        print('value:', i.get('total_value'), '; fraction:', i.get('fraction'))


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    max_value, solution = fractional_knapsack_max_value(wt, val, capacity)
    print("valor máximo =", max_value)
    print_solution(solution)
