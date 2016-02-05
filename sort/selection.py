# 时间复杂度O(n^2), 空间复杂度O(1)

def selection_sort(list):
    for i in range(len(list)):
        min=list[i]
        p=i
        for j in range(i+1,len(list)):
            if list[j]<min:
                p=j
                min=list[j]
        if i!=p:
            list[i],list[p]=list[p],list[i]
    return list

list=[1,3,2,15,6,7,14,21]
print(selection_sort(list))
