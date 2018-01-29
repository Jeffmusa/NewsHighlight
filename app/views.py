from flask import render_template
from app import app
from .request import get_sources

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and 
    its data
    '''

    #get general sources
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')


    title = 'Home - Welcome to the best Online News Website'
    return render_template('index.html',title=title, general=general_sources)

# @app.route('/news/<news_id>')
# def news(news_id):
#     '''
#     view page function that returns the news articles and its data
#     '''
#     title = 'Home - Welcome to the best Online News Website'
#     return render_template('news.html', id=news_id, title=title)