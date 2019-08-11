from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

print('Naziv aktivnog modula je:', __name__)
	
app.run()

"""
Ova veb aplikacija se (u Linuxu) pokreće iz komandne linije pomoću:
$ python3 hello_flask.py
Zatim se u veb brauzeru zadaje adresa:
http://127.0.0.1:5000 ili
http://localhost:5000
"""
