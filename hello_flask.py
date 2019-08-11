from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

print('Naziv aktivnog modula je:', __name__)
	
app.run()
