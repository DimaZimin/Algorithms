import random
from timeit import repeat


def run_sorting_algorithm(algorithm, array):

    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def bubble_sort(array):

    n = len(array)

    for i in range(n):

        already_sorted = True

        for j in range(n - i - 1):

            if array[j] > array[j + 1]:

                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:

            break

    return array


def random_list(m=1000):
    return [random.randint(-m, m) for _ in range(m)]

if __name__ == '__main__':
    array = random_list()
    run_sorting_algorithm(algorithm="bubble_sort", array=array)
    
    # Algorithm: bubble_sort. Minimum execution time: 1.00632117
