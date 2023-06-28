def bubble_sort(a):
    for i in range(0, len(a) - 1):
        already_sorted = True
        for j in range(1, len(a) - i):
            if a[j] < a[j - 1]:
                already_sorted = False
                a[j], a[j - 1] = a[j - 1], a[j]

        if already_sorted and i != 0:
            return
        print(" ".join(map(str, a)))


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    bubble_sort(a)
