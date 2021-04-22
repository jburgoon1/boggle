from boggle import Boggle
from flask import Flask, flash,render_template, request, session, jsonify,json, redirect
from boggle import Boggle




boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/boggle', methods = ['GET','POST'])
def show_game():
    session['board']=Boggle().make_board()
    return render_template('game.html', board = session['board'], result = result )

@app.route('/answer', methods = ['GET', 'POST'])
def check_word():
    if request.method == 'POST':
        json_data = request.form.get('guess')
    if Boggle().check_valid_word(session['board'], json_data):
        flash('congrats you got it right!')
        result = jsonify({'result':'ok'},{'result':'not-on-board'},{'result':'not-a-word'})
        return result 