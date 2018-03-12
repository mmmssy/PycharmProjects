#!/usr/bin/python3
#coding=utf-8

# list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop(0)
# print ("删除的项为 :", list_pop)
# print ("列表现在为 : ", list1)

# def quicksort(nums):
#     if len(nums) <=1:
#         return nums
#     else:
#         less = []    #左边
#         greater = []  #右边
#         tmp = nums.pop(0)   #基数
#
#         for i in nums:
#             if i < tmp:
#                 less.append(i)
#             else:
#                 greater.append(i)
#         return quicksort(less) + [tmp] +quicksort(greater)
#
# def main():
#     nums = [6,7,2,1,3,9]
#     print("排序结果为:", quicksort(nums))
# main()

num = [6,7,2,1,3,9]
tmp = num.pop(0)
print(num)
print(tmp)

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        left = []
        right = []
        tmp = lst.pop(0)

        for i in lst:
            if i < tmp:
                left.append(i)
            else:
                right.append(i)
        return quicksort(left) + tmp +quicksort(right)

def main():
    lst = [6,7,2,1,9,3]
    print('排序結果爲:',quicksort(lst))
main()