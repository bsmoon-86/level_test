from database import MyDB1


mydb = MyDB1()


table1 = """
    create table 
    if not exists
    test_table (
        No int primary key, 
        question text not null, 
        a1 text not null, 
        a2 text not null, 
        a3 text not null, 
        a4 text not null, 
        answer int not null

    )
"""

table2 = """
    create table 
    if not exists
    answer_table (
        name varchar(32) primary key, 
        q1 int not null, 
        q2 int not null, 
        q3 int not null, 
        q4 int not null, 
        q5 int not null, 
        q6 int not null, 
        q7 int not null, 
        q8 int not null, 
        q9 int not null, 
        q10 int not null, 
        score int not null
    )
"""

mydb.sql_query(table1)
mydb.sql_query(table2)