from flask import render_template, request
from app import app
from modules.game import two_player, single_player, single_player_spock
from modules.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')

@app.route('/<choice_1>/<choice_2>')
def score(choice_1, choice_2):
    pass

@app.route('/tprps')
def tprps():
    return render_template('/tprps.html', title='2 Player Rock Paper Scissors')

@app.route('/tprps', methods = ["POST"])
def tprps_form():
    player1_name = request.form['name1']
    choice_1 = request.form['player1_choice']
    player2_name = request.form['name2']
    choice_2 = request.form['player2_choice']
    player_1 = Player(name=player1_name, choice=choice_1)
    player_2 = Player(name=player2_name, choice=choice_2)
    two_player(player_1, player_2)

@app.route('/tprpsls')
def tprpsls():
    return render_template('/tprpsls.html', title='2 Player Rock Paper Scissors Lizard Spock')

@app.route('/oprps')
def oprps():
    return render_template('/oprps.html', title='1 Player Rock Paper Scissors')

@app.route('/oprpsls')
def oprpsls():
    return render_template('/oprpsls.html', title='1 Player Rock Paper Scissors Lizard Spock')
