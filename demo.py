def cal_volume(r, h):
    pi = 3.14
    res = pi * r * r * h
    print(res)
    return res


# cal_volume(2, 3)

def find_common(num1, num2):
    max_res = min(num1, num2)   # min_res

    while max_res > 0:
        if num1 % max_res == 0 and num2 % max_res == 0:
            print(max_res)
            return max_res
        else:
            max_res -= 1


find_common(10, 50)


def searchInsert(nums, target): # sorted list is needed for the value nums

    for key, value in enumerate(nums):
        if value == target:
            return key

        if value > target:
            return key

    return len(nums)


def search(nums, target):

    for index, value in enumerate(nums):
        if value == target:
            return index

    return -1

# print(search([1, 2, 3], 2))


def romanToInt( s):
    convertedInt = 0
    romanHashmap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    prevChar = None
    for letter in s:
        currChar = letter
        if prevChar is not None and  romanHashmap[currChar] > romanHashmap[prevChar]:
            convertedInt = convertedInt - 2 * romanHashmap[prevChar] + romanHashmap[currChar]
        else:
            convertedInt += romanHashmap[currChar]
        prevChar = currChar

    return convertedInt


print(romanToInt("CLV"))


def run_sum(nums):
    v = 0
    l = []
    for i in nums:
        v = v + i
        l.append(v)
    print(l)

run_sum([1, 2, 3])





