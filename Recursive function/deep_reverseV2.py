def deep_reverse(lst):
    return list(reversed([item if not isinstance(item, list) else deep_reverse(item) for item in lst]))


if __name__ == '__main__':
    lst = [[1, 2, 3], [4, 5, 6], 8, 7]
    lst.reverse()
    print(lst)
    lst = [[1, 2, 3], [4, 5, 6], 8, 7]
    deep_reverse(lst)
    print(lst)