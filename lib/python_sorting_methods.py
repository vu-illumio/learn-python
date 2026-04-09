
def count_sort(elist):
    count = [0 for _ in range(max(elist)+1)]
    while len(elist) > 0:
        e = elist.pop()
        count[e] += 1
    for e in range(len(count)):
        while count[e] > 0:
            elist.append(e)
            count[e] -= 1
    return elist

def insertion_sort(elist):
    for n in range(1, len(elist)):
        sort_item = elist[n]
        sort_idx = n
        while sort_idx > 0 and sort_item < elist[sort_idx-1]:
            print(f'shift {elist[sort_idx-1]} to index {sort_idx}')
            elist[sort_idx] = elist[sort_idx-1]
            sort_idx -= 1
        if sort_idx != n:
            print(f'insert {sort_item} at index {sort_idx}')
            elist[sort_idx] = sort_item
        else:
            print(f'keep {sort_item} at index {sort_idx}')

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
        i = n
        for m in range(n+1, len(elist)):
            if elist[i] > elist[m]:
                i = m
        if n != i:
            print(f'swap {n} {i}')
            elist[n], elist[i] = elist[i], elist[n]

def bubble_sort(elist):
    swap = True
    n = len(elist)
    while swap:
        swap = False
        for i in range(1, n):
            if elist[i] < elist[i-1]:
                print(f'swap {i} {i-1}')
                swap = True
                elist[i], elist[i-1] = elist[i-1], elist[i]
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
    pass
    
---
