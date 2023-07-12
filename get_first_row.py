def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
    w = open(data, mode= 'r')
    a = w.read()
    list1 = []
    list2 = []
    for i in a.split('\n'):
        list1.append(i.split(','))

   return list1[0]
   
   print(get_first_row('data.csv'))