def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    """ a=True
    ind=0
    b=list1[ind]
    ind+=1 
    if list1[ind]==b and type(list1[ind])==type(b):
        pass
    else: 
        a=False
    ind+=1
    if list1[ind]==b and type(list1[ind])==type(b):
        pass
    else: 
        a=False
    ind+=1
    if list1[ind]==b and type(list1[ind])==type(b):
        pass
    else: 
        a=False
    ind+=1
    if list1[ind]==b and type(list1[ind])==type(b):
        a=True
    else: 
        a=False
    return a
    
list1=[1,True,1,True,1]
print(main(list1))

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
    
list1=[1,1,1,True,1]
print(main(list1))