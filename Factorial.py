def permutations(arr, path=[], result=[]):
    if not arr: # arr == []
        result.append(path)
    for i in range(len(arr)):
        permutations(arr[:i] + arr[i+1:], path + [arr[i]], result)
    return result

# i = 0
# arr[:0] + arr[1:] = [2, 3]
# path + [arr[0]] = [1]
# permutations([2, 3], [1])

# 呼叫並取得所有排列
all_perms = permutations([1, 2, 3])
print(all_perms)