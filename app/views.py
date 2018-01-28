from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and 
    its data
    '''
    title = 'Home - Welcome to the best Online News Website'
    return render_template('index.html',title=title)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    view page function that returns the news articles and its data
    '''
    title = 'Home - Welcome to the best Online News Website'
    return render_template('news.html', id=news_id, title=title)