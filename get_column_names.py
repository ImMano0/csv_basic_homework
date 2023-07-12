#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    w=open(data, mode='r')
    a=w.read()
    list1 = []
    for i in a.split('\n'):
        list1.append(i)
    
    return list1[0]
print(get_column_names('data.csv'))