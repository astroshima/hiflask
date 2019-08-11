from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

print('Naziv aktivnog modula je:', __name__)

if __name__=='__main__':    # ako je ovaj program startovan komandom python3
    app.run()               # pokreni veb server i aplikaciju

"""
Podešavanje promenljive okruženja i startovanje veb servera i aplikacije iz komandne linije:
$ env FLASK_APP=hello_flask_1_1.py flask run
"""
