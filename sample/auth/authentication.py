from flask import request, jsonify
from sample import api
from sample import db
from . import auth
from store import TokenStore, generate_token
from user import User, Client

auth.route('/oauth', method=['POST'])
def access():
    username = request.form.get('username')
    passwd = request.form.get('password')
    uid = request.form.get('user_id')
    client_id = request.form.get('client_id')
    secret = request.form.get('client_secret')
    u = User.query.get_or_404(username)