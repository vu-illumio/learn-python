
def count_sort(elist):
    if len(elist) == 0:
        return elist
    min_e = min(elist)
    max_e = max(elist)
    count = [0 for _ in range(max_e - min_e + 1)]
    while len(elist) > 0:
        e = elist.pop()
        count[e - min_e] += 1
    for e in range(len(count)):
        if count[e] > 0:
            elist.extend([e + min_e] * count[e])
    return elist

def insertion_sort(elist):
    for n in range(1, len(elist)):
        if elist[n] >= elist[n-1]:
            # print(f'keep {elist[n]} at index {n}')
            continue
        sort_e = elist[n]
        sort_idx = n
        while sort_idx > 0 and sort_e < elist[sort_idx-1]:
            # print(f'shift {elist[sort_idx-1]} to index {sort_idx}')
            elist[sort_idx] = elist[sort_idx-1]
            sort_idx -= 1
        # print(f'insert {sort_e} at index {sort_idx}')
        elist[sort_idx] = sort_e

# def insertion_sort(elist):
#     for n in range(1, len(elist)):
#         if elist[n] >= elist[n-1]:
#             print(f'skip {elist[n]} at index {n}')
#             continue
#         e = elist.pop(n)
#         if e < elist[0]:
#             elist.insert(0, e)
#             print(f'insert {e} at index 0')
#         else:
#             for m in range(n-2, -1, -1):
#                 if e >= elist[m]:
#                     elist.insert(m+1, e)
#                     print(f'insert {e} at index {m+1}')
#                     break
#                 else:
#                     print(f'check index {m}')

def selection_sort(elist):
    for n in range(len(elist)-1):
        min_idx = n
        for m in range(n+1, len(elist)):
            if elist[min_idx] > elist[m]:
                min_idx = m
        if n != min_idx:
            print(f'swap {n} {min_idx}')
            elist[n], elist[min_idx] = elist[min_idx], elist[n]

def bubble_sort(elist):
    swap = True
    n = len(elist)
    while swap:
        swap = False
        for m in range(1, n):
            if elist[m] < elist[m-1]:
                print(f'swap {m} {m-1}')
                swap = True
                elist[m], elist[m-1] = elist[m-1], elist[m]
        n -= 1

# def bubble_sort(elist):
#     for n in range(len(elist)-1):
#         swap = False
#         for m in range(1, len(elist)-n):
#             if elist[m] < elist[m-1]:
#                 print(f'swap {m} {m-1}')
#                 swap = True
#                 elist[m], elist[m-1] = elist[m-1], elist[m]
#         if not swap:
#             break

def merge_sort(elist):
    if len(elist) <= 1:
        return elist
    else:
        mid = len(elist)//2
        left = merge_sort(elist[:mid])
        right = merge_sort(elist[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]
