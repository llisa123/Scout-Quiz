from flask import Flask, render_template, request, redirect, g
import sqlite3
app = Flask(__name__)

all_questions = []
all_answers = []

@app.route('/')
def quiz():
    all_questions = []
    for question in g.db.execute("SELECT * FROM all_questions"):
        # import pdb;pdb.set_trace()
        all_questions.append({
            'question': question[0],
            'answer': question[1],
            'options': question[2].split("\n")
        })
    return render_template('index.html', all_questions=all_questions)

@app.route('/submit', methods = ['POST'])
def submit():
    # import pdb;pdb.set_trace()
    rightansweres = []
    answercount=0
    answercorrect=0
    for question in g.db.execute("SELECT * FROM all_questions"):
        rightansweres.append(question[1])
    for answer in g.db.execute("SELECT question, answer FROM all_questions"):
        givenanswer=request.form[answer[0]].strip()
        print(givenanswer)
        answercount+=1
        if givenanswer in rightansweres:
            print('correct')
            answercorrect+=1
        else:
            print('false')
    result = 100*answercorrect/answercount
    print(result)
    return render_template('result.html', result=result)

@app.route('/goback', methods = ['POST'])
def goback():
    return redirect('/')

@app.route('/questions.html')
def questions():
    return render_template('questions.html')

@app.route('/submitquestion', methods = ['POST'])
def submitquestion():
    newquestion = request.form['newquestion']
    all_questions.append(newquestion)
    print(all_questions)
    newanswer = request.form['newanswer']
    all_answers.append(newanswer)
    print(all_answers)
    options = request.form['options']
    g.db.execute("INSERT INTO all_questions (question, answer, answer_options) VALUES ('{newquestion}', '{newanswer}', '{options}')".format(newquestion=newquestion, newanswer=newanswer, options=options))
    g.db.commit()
    return redirect('/')

@app.before_request
def before_request():
    g.db = sqlite3.connect("questions.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ =='__main__':
    app.run()
