from flask import render_template, request
from app import app
from modules.game import two_player, single_player, single_player_spock
from modules.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')

