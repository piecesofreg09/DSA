# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    res = []
    if numbers[0] > numbers[1]:
        res = [numbers[0], numbers[1]]
    else:
        res = [numbers[1], numbers[0]]
        
    for it in range(2, n):
        if numbers[it] >= res[0]:
            res = [numbers[it], res[0]]
        else:
            if numbers[it] >= res[1]:
                res = [res[0], numbers[it]]

    return res[0] * res[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
