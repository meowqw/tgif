from app import db, app
from flask import Flask, jsonify, render_template, url_for, request, redirect, flash, request
from app.models import AccessKeys, Objects, Users, UserAdmin, Chats
from flask_login import login_user, login_required, logout_user


# ***************** ENTRY ******************
@app.route('/entry', methods=['POST', 'GET'])
def entry():
    """Render Entry page"""

    return render_template('entry.html', active='entry')


# ***************** FAQ ******************
@app.route('/faq', methods=['POST', 'GET'])
def faq():
    """Render FAQ page"""

    return render_template('faq.html', active='faq')


# ***************** INDEX ******************
@app.route('/', methods=['POST', 'GET'])
def index():
    """Render main page"""

    return render_template('index.html', active='index')


# ***************** NEWS-PAGE ******************
@app.route('/news/page', methods=['POST', 'GET'])
def news_page():
    """Render NEWS-PAGE page"""

    return render_template('news-page.html', active='news-page')


# ***************** NEWS ******************
@app.route('/news', methods=['POST', 'GET'])
def news():
    """Render news page"""

    return render_template('news.html', active='news')


# ***************** WALLETS ******************
@app.route('/wallets', methods=['POST', 'GET'])
def wallets():
    """Render wallets page"""

    return render_template('wallets.html', active='wallets')

# ***************** REQUEST ******************
@app.route('/request', methods=['POST', 'GET'])
def request():
    """Render request page"""

    return render_template('request.html', active='request')