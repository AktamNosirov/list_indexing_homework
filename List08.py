def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    ind=0
    if list1[ind]==0 :
        list1[ind]=False
    if list1[ind]==1 :
        list1[ind]=True
    ind+=1
    if list1[ind]==0 :
        list1[ind]=False
    if list1[ind]==1 :
        list1[ind]=True
    ind+=1   
    if list1[ind]==0 :
        list1[ind]=False
    if list1[ind]==1 :
        list1[ind]=True
    ind+=1
    if list1[ind]==0 :
        list1[ind]=False
    if list1[ind]==1 :
        list1[ind]=True
    ind+=1
    if list1[ind]==0 :
        list1[ind]=False
    if list1[ind]==1 :
        list1[ind]=True
    return list1
        
list1=[0,0,1,0,1]
print(main(list1))
