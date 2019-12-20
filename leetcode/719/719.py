def solve(a, k):
    a = sorted(a)

    n = len(a)
    l = 0
    r = a[-1] - a[0]

    ret = 0
    while l < r:
        mid = (l + r) / 2

        x = 0
        y = 0
        count = 0

        while y < n:
            while x < y and a[y] - a[x] > mid:
                x += 1
            count += y - x
            y += 1

        print l, r, mid, ret
        if count < k:
            l = mid + 1
        else:
            r = mid
    return r



a = [1, 6, 1]
a = [62,100,4]
k = 2
print solve(a, k)
