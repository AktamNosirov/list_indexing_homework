def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    ind=0
    b=list1[ind]
    ind+=1 
    if list1[ind]==b and type(list1[ind])==type(b) :
        ind+=1
    if list1[ind]==b and type(list1[ind])==type(b):
        ind+=1
    if list1[ind]==b and type(list1[ind])==type(b):
        ind+=1
    if list1[ind]==b and type(list1[ind])==type(b):
        return True
    else: 
        return False
    
list1=[1,True,1,True,1]
print(main(list1))