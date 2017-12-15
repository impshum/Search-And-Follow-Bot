import sys
import tweepy
import time
import random
from config import *


class Colour:
    Green, Red, White, Yellow = '\033[92m', '\033[91m', '\033[0m', '\033[93m'

print(Colour.Yellow + """
 _______ _______ _______  ______ _______ _     _    / _______  _____                 _____  _  _  _
 |______ |______ |_____| |_____/ |       |_____|   /  |______ |     | |      |      |     | |  |  |
 ______| |______ |     | |    \_ |_____  |     |  /   |       |_____| |_____ |_____ |_____| |__|__|
                                                 /
""")

mins = timer / 60
print(Colour.White + 'Searching every {}'.format(int(mins)),
      'minutes\n\nPress Ctrl + C to exit\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

d = time.strftime('%a %H:%M:%S')

p2 = 'putln2'

if follow:
    try:
        api.create_friendship(p2)
    except tweepy.TweepError as e:
        print(e, '\n')

def searchfollow():
    tag = random.choice(search)
    twt = api.search(q=tag, count=count, lang='en', result_type='recent')

    try:
        for s in twt:
            if tag in s.text:
                sn = s.user.screen_name
                m = '@' + sn
                tweet = random.choice(message)
                out = m, tweet
                print(Colour.Green + '\n' + d)
                print(Colour.Green + 'Searching for:', tag)
                time.sleep(1)
                print(Colour.Green + 'Found:', s.text)
                time.sleep(3)
                print(Colour.Green + 'Tweeting:', ' '.join(out))
                api.update_status(' '.join(out), in_reply_to_status_id=s.id)
                time.sleep(3)

                if not s.user.following:
                    # s.user.follow()
                    print(Colour.Green + 'Following: @' + sn)
                    time.sleep(5)
                else:
                    print(Colour.Red + 'Already following: @' + sn)
                    time.sleep(5)
    except tweepy.TweepError as e:
        print(Colour.Red + d, 'FAIL', e.reason, '\n')
        time.sleep(10)


while True:
    try:
        searchfollow()
        print('\nSleeping...')
        time.sleep(timer)
    except KeyboardInterrupt:
        print(Colour.White + '\nExiting\n')
        sys.exit(1)
