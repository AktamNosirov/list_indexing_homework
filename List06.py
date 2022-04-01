def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    ind=0
    if list1[ind]==1 :
        list1[ind]="true"
    else:
        list1[ind]=0
    ind+=1
    if list1[ind]==1 :
        list1[ind]='true' 
    else:
        list1[ind]=0
    ind+=1   
    if list1[ind]==1 :
        list1[ind]='true'
    else:
        list1[ind]=0    
    ind+=1
    if list1[ind]==1 :
        list1[ind]='true'
    else:
        list1[ind]=0
    ind+=1
    if list1[ind]==1 :
        list1[ind]='true'
    else:
        list1[ind]=0
        return list1
        
list1=[1,1,1,1,1]
print(main(list1))