import pandas as pd
from database import MyDB1

mydb = MyDB1()

df = pd.read_excel('test_table.xlsx')

df['q'] = df['q'].str.replace('\xa0', ' ')

for i in range(len(df)):
    insert_query = """
        insert into test_table
        (`question`, `a1`, `a2`, `a3`, `a4`, `answer`) 
        values 
        (%s, %s, %s, %s, %s, %s)
    """
    data = df.loc[i, ].to_list()
    try:    
        mydb.sql_query(insert_query, data)
    except:
        print('sql error')