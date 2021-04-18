from flask import render_template, request
from app import app
from modules.game import *
from modules.player import *

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
    player_1 = Player(name=player1_name)
    player_1.make_choice(choice_1)
    player_2 = Player(name=player2_name)
    player_2.make_choice(choice_2)
    play_game = Game(player_1, player_2)
    result = play_game.result(player_1, player_2)
    return render_template('score.html', title='Winner Is', result=result, player_1=player_1, player_2=player_2)

@app.route('/tprpsls')
def tprpsls():
    return render_template('/tprpsls.html', title='2 Player Rock Paper Scissors Lizard Spock')

@app.route('/tprpsls', methods = ["POST"])
def tprpsls_form():
    player1_name = request.form['name1']
    choice_1 = request.form['player1_choice']
    player2_name = request.form['name2']
    choice_2 = request.form['player2_choice']
    player_1 = Player(name=player1_name)
    player_1.make_choice(choice_1)
    player_2 = Player(name=player2_name)
    player_2.make_choice(choice_2)
    play_game = Game(player_1, player_2)
    result = play_game.result(player_1, player_2)
    return render_template('score2.html', title='Winner Is', result=result, player_1=player_1, player_2=player_2)

@app.route('/oprps')
def oprps():
    return render_template('/oprps.html', title='1 Player Rock Paper Scissors')

@app.route('/oprps', methods = ["POST"])
def oprps_form():
    player1_name = request.form['name1']
    choice_1 = request.form['player1_choice']
    player_1 = Player(name=player1_name)
    player_1.make_choice(choice_1)
    player_2 = Player("A.I.")
    play_game = Game(player_1, player_2)
    result = play_game.computer_rps(player_1, player_2)
    return render_template('score.html', title='Winner Is', result=result, player_1=player_1, player_2=player_2)

@app.route('/oprpsls')
def oprpsls():
    return render_template('/oprpsls.html', title='1 Player Rock Paper Scissors Lizard Spock')

@app.route('/oprpsls', methods = ["POST"])
def oprpsls_form():
    player1_name = request.form['name1']
    choice_1 = request.form['player1_choice']
    player_1 = Player(name=player1_name)
    player_1.make_choice(choice_1)
    player_2 = Player("A.I.")
    play_game = Game(player_1, player_2)
    result = play_game.computer_rpsls(player_1, player_2)
    return render_template('score2.html', title='Winner Is', result=result, player_1=player_1, player_2=player_2)