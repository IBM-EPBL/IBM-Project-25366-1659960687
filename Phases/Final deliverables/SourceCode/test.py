from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='0ec740dfc1fc459a8ab653d0b9748424')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
                                          category='business',
                                          language='en')

print(top_headlines)