def deep_reverse(lst):
    for item in lst:
        if isinstance(item, list):
            deep_reverse(item)
    lst.reverse()

if __name__ == '__main__':
    lst = [[1, 2, 3], [4, 5, 6], 8, 7]
    lst.reverse()
    print(lst)
    lst = [[1, 2, 3], [4, 5, 6], 8, 7]
    deep_reverse(lst)
    print(lst)