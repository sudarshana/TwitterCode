import twitter

api = twitter.Api(
 consumer_key='Consumer Key here',
 consumer_secret='Consumer Secret here',
 access_token_key='Access Token Key here',
 access_token_secret='Access Token Secret here'
 )

search = api.GetSearch(term='google', lang='en', result_type='popular', count=100)
for term in search:
 print term.user.screen_name + ' (' + term.created_at + ')' + ' (' + term.geocode + ')' 
 print term.text.encode('utf-8')
 print ''
