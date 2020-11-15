import time
import tweepy
import yaml

from main import Runner
from consts.player_list import PLAYERS

with open('secret.yaml') as secret:
    cfg = yaml.load(secret)

# print(cfg['twitter']['api_key'])

auth = tweepy.OAuthHandler(cfg['twitter']['api_key'], cfg['twitter']['api_key_secret'])
auth.set_access_token(cfg['twitter']['access_token'], cfg['twitter']['access_token_secret'])

api = tweepy.API(auth)

def run():
    runner = Runner(PLAYERS)
    api.update_status(runner.question())
    print("Posted question tweet, sleeping...")
    time.sleep(30)
    print("Finished sleeping...")
    api.update_status(runner.answers())
    print("Posted answer")

run()