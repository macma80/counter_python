import numpy as np


def count_less_or_equal_brute_force(equipo_a: list, equipo_b: list):
    """
    Counts the number of elements in `equipo_a` that are less than or equal to each element in `equipo_b`.

    This function uses a brute-force approach to iterate over each element in `equipo_b` and counts
    how many elements in `equipo_a` are less than or equal to it. The result is a list where each
    element corresponds to the count for each element in `equipo_b`.
    Because of the nested loop, the time complexity of this approach is O(m x n)
    where m is the number of elements in equipo_b and n is the number of elements in equipo_a.
    :param equipo_a:
    :param equipo_b:
    :return:
    """
    result = []
    for b in equipo_b:
        count = sum(1 for a in equipo_a if a <= b)
        result.append(count)
    return result


def count_less_or_equal_numpy(equipo_a: list, equipo_b: list):
    """
    Function counts the number of elements in `equipo_a` that are less than or equal to each element in `equipo_b`.
    Since the lists have only numerical values, this function uses NumPy to take advantage of its efficient
    computations.
    Overall, the time complexity is approximately O(m x n), but with faster computations due to NumPy’s optimizations.
    :param equipo_a:
    :param equipo_b:
    :return:
    """
    equipo_a = np.array(equipo_a)
    equipo_b = np.array(equipo_b)
    results = np.array([np.sum(equipo_a <= b) for b in equipo_b])
    return results.tolist()


if __name__ == '__main__':
    list_a = [2, 10, 5, 4, 8]
    list_b = [3, 1, 7, 8]

    print(count_less_or_equal_brute_force(list_a, list_b))
    print(count_less_or_equal_numpy(list_a, list_b))
