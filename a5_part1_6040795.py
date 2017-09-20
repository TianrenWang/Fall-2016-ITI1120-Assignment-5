# Course: ITI 1120
# Assignment # 5 Part 1
# Wang, Tianren
# 6040795

def largest_34(a):
    '''(list)->int
    Returns the sum of the 3rd and 4th largest values in the list a
    Precondition: a has at least 4 elements
    '''
    
    temp_list = []
    for item in a:
        temp_list.append(item)

    biggest = max(temp_list)
    temp_list.pop(temp_list.index(biggest))
    second_biggest = max(temp_list)
    temp_list.pop(temp_list.index(second_biggest))
    third_biggest = max(temp_list)
    temp_list.pop(temp_list.index(third_biggest))
    fourth_biggest = max(temp_list)
    temp_list.pop(temp_list.index(fourth_biggest))
    return fourth_biggest + third_biggest

def largest_third(a):
    '''(list)->int
    Returns the sum of the len(a)//3 of the largest values in the list a
    Precondition: Numbers in the list a are all distinct and that the
    list a has at least 3 elements
    '''
    
    temp_list = []
    for item in a:
        temp_list.append(item)

    temp_list.sort()

    return sum(temp_list[-len(a)//3:])

def third_at_least(a):
    '''(list)->int
    Returns a value in a that occurs at least len(a)//3 + 1 times.
    If no such element exists in a, then this function returns None.
    Precondition: None
    '''
    
    temp_list = []
    for item in a:
        temp_list.append(item)

    temp_list.sort()
    
    times = len(a)//3 + 1
    counter = 0
    for i in range(len(temp_list)):
        if i + times < len(temp_list) and temp_list[i] == temp_list[i + times-1]:
            return temp_list[i]

    return None

def sum_tri(a,x):
    '''(list)->bool
    Returns whether there exists indices i, j and k such that
    a[i]+a[j]+a[k]=x.
    Precondition: None
    '''
    temp_list = []
    for item in a:
        temp_list.append(item)

    temp_list.sort()
    
    for i in range(len(temp_list)):
        j = 0
        k = len(a) - 1
        
        while j != k:
            temp_sum = temp_list[i] + temp_list[j] + temp_list[k]
            if temp_sum == x:
                return True
            elif temp_sum < x:
                j += 1
            elif temp_sum > x:
                k -= 1

    temp_sum = temp_list[i] + temp_list[j] + temp_list[k]
    if temp_sum == x:
        return True
    return False
