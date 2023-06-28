def merge(arr, lf, mid, rg):
    i = lf
    j = mid
    result = []
    while i < mid and j < rg:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    while i < mid:
        result.append(arr[i])
        i += 1
    while j < rg:
        result.append(arr[j])
        j += 1

    j = 0
    for i in range(lf, rg):
        arr[i] = result[j]
        j += 1
    return arr


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return arr

    middle = (lf + rg) // 2

    merge_sort(arr, lf, middle)
    merge_sort(arr, middle, rg)

    return merge(arr, lf, middle, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
