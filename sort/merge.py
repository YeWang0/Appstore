def merge(left,right):
    r=0
    l=0
    result=[]
    while l<len(left) and  r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    if l<len(left):
        for x in left[l:]:
            result.append(x)
    else:
        for x in right[r:]:
            result.append(x)
    # print(result)
    return result
def merge_sort(list):
    if len(list)<=1:
        return list
    n=len(list)/2
    return merge(merge_sort(list[:n]),merge_sort(list[n:]))




print merge_sort([1,3,5,21,4,6,6,4,33,2,2,31,5,12])