from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/<user_id>')    #za URL putanju '/<user_id>' pozovi funkciju getUser i prosledi joj string 'user_id'
def getUser(user_id):
    return 'I am user: %s.' % user_id

if __name__=='__main__':
    app.run()
