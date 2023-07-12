import csv 

def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open(data, mode='r')
    r=f.read()
    
    list1=[]

    list2=[]

    for i in r.split('\n'):
        list1.append(i.split(','))

    for k in list1:
        list2.append(k[0])

    return list2

print(get_first_column('data.csv'))