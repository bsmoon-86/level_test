from flask import Flask, request, render_template
import pymysql
from database import MyDB1

app = Flask(__name__)

mydb = MyDB1()

@app.route('/')
def level_test():
    query1 = """
        select `No`, `question`, `a1`, `a2`, `a3`, `a4` from test_table
    """
    data = mydb.sql_query(query1)
    return render_template('test.html', data = data, cnt = len(data))

@app.route('/submit', methods=['post'])
def answer_submit():
    answers = dict(request.form)
    query2 = """
        select `answer` from test_table
    """
    data = mydb.sql_query(query2)
    #print(data)
    #print(answers)
    insert_data = [answers['user']]
    answer_cnt = 0
    for a_key, answer in zip(answers, data):
        insert_data.append(int(answers[a_key]))
        if int(answers[a_key]) == int(answer['answer']):
            answer_cnt += 1
    
    insert_data.append(answer_cnt * 10)
    insert_query = """
        insert into answer_table 
        values 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    print(len(insert_data))
    db_res = mydb.sql_query(insert_query, insert_data)
    print(answers['user'], db_res)
    return str(answer_cnt * 10)







app.run(debug=True)