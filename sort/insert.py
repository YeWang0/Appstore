# 时间复杂度O(n^2), 空间复杂度O(1)

def insertion_sort(list):
    print(len(list))
    for i in range(1,len(list)):
        if list[i]<list[i-1]:
            tmp=list[i]
            index=i
            print tmp,i
            for j in range(i-1,0,-1):
                print(list[j],tmp)
                if tmp<list[j]:
                    list[j+1]=list[j]
                    index=j
                    # print("list:")
                    # print(list)
                else:
                    break
            list[index]=tmp
    return list

list=[1,3,2,15,6,7,14,2]
print(insertion_sort(list))