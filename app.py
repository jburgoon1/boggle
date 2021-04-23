from boggle import Boggle
from flask import Flask, flash,render_template, request, session, jsonify,json, redirect,url_for





boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'


@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/boggle', methods = ['GET','POST'])
def show_game():
    
    session['board']=Boggle().make_board()
    return render_template('game.html', board = session['board'] )

@app.route('/answer', methods = ['GET', 'POST'])

def check_word():
    count = 0
    guess = request.form.get('guess')

    print(guess)
    if boggle_game.check_valid_word(session['board'], guess) == 'ok':
        result = 'ok'
        count += len(guess)
        print(count)
        return redirect(url_for('show_game'))
    elif boggle_game.check_valid_word(session['board'], guess) == 'not-on-board':
        result = 'Not on the board'
        count += 0
    else:
        result = 'Not a word' 
        count += 0

    return render_template('game.html', board = session['board'], result = result, count = count)