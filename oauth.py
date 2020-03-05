from twython import Twython

APP_KEY = 'JyvKTUU98cMCIhhWC0MiMcwmZ'
APP_SECRET = 'ZAgycA8nHsLf0KmGbjCm83Pvhe8vLX4C6dUy517Wfoe8GZJmKl'

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
print(auth)


OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']


twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

oauth_verifier =input("Enter code : ")
final_step = twitter.get_authorized_tokens(oauth_verifier)



OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

print("OAUTH_TOKEN is : ")
print(OAUTH_TOKEN)

print("OAUTH_TOKEN SECRET is : ")
print(OAUTH_TOKEN_SECRET)