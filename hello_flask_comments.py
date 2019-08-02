from flask import Flask     # iz modula flask uvezi klasu Flask

app = Flask(__name__)       # napravi objekat tipa Flask i dodeli ga promenljivoj app
                            # __name__ : vrednost imena trenutno aktivnog modula
@app.route('/')             # dekorator funkcije; kada Flaskov veb server dobije zahtev sa URL putanjom '/', pozovi funkciju hello() 
def hello() -> str:         # definiši funkciju hello(), funkcija vraća string.
    return 'Hello world from Flask!'
	
app.run() # pokreni veb server (tj. veb aplikaciju)
