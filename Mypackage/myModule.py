def top_n(items,n):
    """ Return the top n items in an array, in desc order.

    Args:
        items(array): list or array-like object
        n(int): number of items to return

    Return:
        array: top n items, in desc order
    Egs:
        >>> top_n([8,3,2,7,4],3)
        [8,7,4]
    """
    for i in range(n): # Keep sorting until the top n times
        for j in range(len(items)-1-i):
            if tems[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    #get the last two items
    top_n=items[-n:]
    #return in desc order
    return top_n[::-1]