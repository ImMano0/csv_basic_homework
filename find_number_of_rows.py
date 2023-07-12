def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f = open(data, mode='r')
    w = f.read()
    list1 = []
    for i in w.split('\n'):
        list1.append(i.split(','))
    
    a=0
    for c in list1:
        a+=1

    return a

print(find_number_of_rows('data.csv'))