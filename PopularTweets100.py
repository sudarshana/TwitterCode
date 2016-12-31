import twitter #Wrapper needed - https://pypi.python.org/pypi/python-twitter/

api = twitter.Api(
 consumer_key='Consumer Key here',
 consumer_secret='Consumer Secret here',
 access_token_key='Access Token Key here',
 access_token_secret='Access Token Secret here'
 )

query = raw_input('Term you want to search for: '), 
search = api.GetSearch(term=query, lang='en', result_type='popular', count=100)
# query is what you are looking for. Example: term="cake" 
# result_type also takes 'mixed' and 'recent' https://dev.twitter.com/rest/reference/get/search/tweets
# count shows number of tweets
for term in search:
 print term.user.screen_name + ' (' + term.created_at + ')'  
 print term.text.encode('utf-8')
 print ''
