Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conn = sqlite3.connect("questions.db")
>>> cursor = conn.cursor()
>>> cursor.execute("CREATE TABLE all_questions ( newquestion TEXT );")
<sqlite3.Cursor object at 0x7f8f28604ea0>
>>> cursor.execute("CREATE TABLE all_questions ( question TEXT );")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    cursor.execute("CREATE TABLE all_questions ( question TEXT );")
sqlite3.OperationalError: table all_questions already exists
>>> cursor.execute("ALTER TABLE all_questions ( newquestion TEXT, newanswer TEXT );")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cursor.execute("ALTER TABLE all_questions ( newquestion TEXT, newanswer TEXT );")
sqlite3.OperationalError: near "(": syntax error
>>> conn = sqlite3.connect("questions.db")
>>> cursor = conn.cursor()
>>> cursor.execute("CREATE TABLE all_questions ( question TEXT, answer TEXT );")
<sqlite3.Cursor object at 0x7f8f2675cc70>
>>> cursor.execute("ALTER TABLE all_questions ADD answer_options TEXT")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cursor.execute("ALTER TABLE all_questions ADD answer_options TEXT")
sqlite3.OperationalError: attempt to write a readonly database
>>> conn = sqlite3.connect("questions.db")
>>> 
KeyboardInterrupt
>>> cursor = conn.cursor()
>>> cursor.execute("CREATE TABLE all_questions ( question TEXT, answer TEXT, answer_options TEXT );")
<sqlite3.Cursor object at 0x7f8f28604ea0>
>>> 
