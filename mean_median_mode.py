n = int(input())
arr = list(map(int,input().split()))


def find_mean(arr, n):
    mean = round(sum(arr)/n,1)
    return mean

def find_median(arr, n):
    arr.sort()
    if (n % 2 == 0):
        med = round(((arr[int(n/2)] + arr[int((n/2)-1)])/2),1)
    else:
        med = int((arr[n//2]))
    return med

def find_mode(arr, n):
    temp_arr = arr.copy()
    temp_arr = [str(t) for t in temp_arr]
    occ_arr = {}
    remove_dup = [str(l) for l in list(dict.fromkeys(arr))]
    for r in remove_dup:
        occ_arr[int(r)] = temp_arr.count(r)
    occ_arr = dict(sorted(occ_arr.items()) )
    return max(occ_arr, key=occ_arr.get)

print(find_mean(arr, n))
print(find_median(arr, n))
print(find_mode(arr, n))
