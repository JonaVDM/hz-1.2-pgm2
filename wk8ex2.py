def count_code(str):
    c = 0
    for i in range(0, len(str)-3):
        if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
            c += 1
    return c


def count_hi(str):
    c = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            c += 1
    return c


def end_other(a, b):
    l = min(len(a), len(b))
    x = a[::-1].lower()
    y = b[::-1].lower()
    for i in range(l):
        if x[i] != y[i]:
            return False
    return True


def cat_dog(str):
    cc = 0
    dc = 0

    for i in range(len(str)):
        if str[i:i+3] == 'cat':
            cc += 1
        if str[i:i+3] == 'dog':
            dc += 1

    return cc == dc


def xyz_there(str):
    for i in range(len(str)):
        if i != 0 and str[i-1] == '.':
            continue
        if str[i:i+3] == 'xyz':
            return True
    return False


def count_evens(nums):
    c = 0
    for n in nums:
        if n % 2 == 0:
            c += 1

    return c


def sum13(nums):
    s = 0
    for n in range(len(nums)):
        if nums[n] == 13 or (n != 0 and nums[n-1] == 13):
            continue
        s += nums[n]
    return s


def big_diff(nums):
    small = nums[0]
    big = nums[0]

    for n in nums:
        if small > n:
            small = n
        if big < n:
            big = n
    return big - small


def sum67(nums):
    s = 0
    skip = False
    for n in nums:
        if n == 6:
            skip = True
            continue

        if n == 7 and skip:
            skip = False
            continue

        if skip:
            continue

        s += n
    return s


def centered_average(nums):
    ls = sorted(nums)

    b = 0
    e = len(nums) - 1
    while e - b > 1:
        b += 1
        e -= 1

    return (ls[b] + ls[e]) // 2


def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
