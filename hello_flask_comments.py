from flask import Flask     # iz modula flask uvezi klasu Flask

app = Flask(__name__)       # napravi objekat tipa Flask i dodeli ga promenljivoj app; Flask konstruktor zahteva da mu se prosledi promenljiva __name__
                            # __name__ : promenljiva koja sadrži naziv aktivnog modula (tj. tekućeg imenskog prostora)
@app.route('/')             # dekorator funkcije koji mapira URL putanju (zahteva) na serveru, na akciju kontrolera (tj. funkciju); kada Flaskov veb server dobije zahtev sa URL putanjom '/', pozovi funkciju hello() 
def hello() -> str:         # definiši funkciju hello(), funkcija vraća string.
    return 'Hello world from Flask!'
	
app.run()                   # pokreni veb server i veb aplikaciju
