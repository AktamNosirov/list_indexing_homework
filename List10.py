def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    if list_num[0]>list_num[-1] :
        return list_num[0]
    if list_num[0]<list_num[-1] :
        return list_num[-1]
    if list_num[0]==list_num[-1] :
        return list_num[0:1:-1]
list_num=[1,2,3,4,57,8,1]
print(main(list_num))