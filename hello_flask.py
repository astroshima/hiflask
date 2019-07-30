from flask import Flask		#iz modula flask uvezi klasu Flask

app=Flask(__name__)

@app.route('/')
def hello() -> str:
	return 'Hello world from Flask!'
	
app.run()
