import twitter #Wrapper needed - https://pypi.python.org/pypi/python-twitter/

api = twitter.Api(
 consumer_key='Consumer Key here',
 consumer_secret='Consumer Secret here',
 access_token_key='Access Token Key here',
 access_token_secret='Access Token Secret here'
 )

search = api.GetSearch(term='query here', lang='en', result_type='popular', count=100)
# query is what you are looking for. Example: term="cake" 
# result_type also takes 'mixed' and 'recent'
# count shows the number of tweets
for term in search:
 print term.user.screen_name + ' (' + term.created_at + ')'  
 print term.text.encode('utf-8')
 print ''
