from app import app
import urllib.request
import json
from .models import news_source

#getting api key
api_key = app.config['NEWS_API_KEY']

#getting news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = None
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news results and transform them to a list of objects

    Args:
        sources_list: A list of dictionaries that contain news details

    Returns:
        sources_results: Alist of news source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        if url:
            sources_object = Source(id,name,description,url,category,country)

            sources_results.append(sources_object)
    return sources_results