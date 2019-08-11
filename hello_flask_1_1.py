from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello() -> str:
	return 'Hello world from Flask!'

print('Naziv aktivnog modula je:', __name__)

if __name__=='__main__':	# ako je ovaj program startovan komandom python3
	app.run()				# pokreni server

"""
Startovanje servera iz komandne linije:
$ env FLASK_APP=hello_flask_1_1.py flask run
"""