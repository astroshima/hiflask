from flask import Flask     # iz modula flask uvezi klasu Flask

app = Flask(__name__)       # napravi objekat tipa Flask i dodeli ga promenljivoj app; Flask konstruktor zahteva da mu se prosledi promenljiva __name__
                            # __name__ : promenljiva koja sadrži naziv aktivnog modula (tj. tekućeg imenskog prostora)
@app.route('/')             # dekorator funkcije koji mapira URL putanju (zahteva) na serveru, na akciju kontrolera (tj. funkciju); kada Flaskov veb server dobije zahtev sa URL putanjom '/', pozovi funkciju hello() 
def hello() -> str:         # definiši funkciju hello(), funkcija vraća string.
    return 'Hello world from Flask!'

print('Naziv aktivnog modula je:', __name__)    # ispisuje: Naziv aktivnog modula je __main__ ako startujemo program komandom: $ python3 hello_flask.py
                                                # ispisuje: Naziv aktivnog modula je hello_flask ako startujemo program komandom: $ python3 >>> import hello_flask
app.run()                   # pokreni veb server i veb aplikaciju

"""
Ova veb aplikacija se (u Linuxu) pokreće iz komandne linije pomoću:
$ python3 hello_flask.py
Zatim se u veb brauzeru zadaje adresa:
http://127.0.0.1:5000 ili
http://localhost:5000
"""
