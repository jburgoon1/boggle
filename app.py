from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify,json
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
    if request.method == 'GET':
        json_data = request.get_json('templates/game.html')
        a_value = json.load(json_data)
        value = a_value['words']
        print(value)
    return render_template('game.html', board = session['board'] )


