from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and 
    its data
    '''

    #get general movies
    general = get_sources('general')
    print(general)
    title = 'Home - Welcome to the best Online News Website'
    return render_template('index.html',title=title, general=general)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    view page function that returns the news articles and its data
    '''
    title = 'Home - Welcome to the best Online News Website'
    return render_template('news.html', id=news_id, title=title)