from app import app
import urllib.request
import json
from .models import news_source

#getting api key
api_key = app.config['NEWS_API_KEY']