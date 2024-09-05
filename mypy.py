list1 = [1,2,3,4,5,6]


def summa(index, lst):
    copy_list = lst.copy()
    copy_list.pop(index)
    sum = 1
    for i in copy_list:
        sum *= i

    return sum


def testpy(list1:list):
    result = []
    for i in range(0, len(list1)):
        copy_list = list1.copy()
        sum = 1
        copy_list.pop(i)
        for num in copy_list:
            sum *= num
        result.append(sum)

    return result


print(testpy(list1))



