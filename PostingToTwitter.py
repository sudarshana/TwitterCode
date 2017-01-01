import twitter #Wrapper needed - https://pypi.python.org/pypi/python-twitter/

api = twitter.Api (
 consumer_key = 'Your Consumer Key',
 consumer_secret = 'Your Consumer Secret',
 access_token_key = 'Your Access Token',
 access_token_secret ='Your Access Token Secret'
 ) 

tweet = raw_input ("What do you want to tweet? ")

answer = raw_input ("Do you want the tweet to say - Sent using the Twitter API and Python? (Y/N) ")

if answer == "N":
	status = api.PostUpdate(tweet)
else:
	status = api.PostUpdate(tweet + " - Sent using the Twitter API and Python.")
