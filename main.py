if __name__ == "__main__":
  from requests_oauthlib import OAuth1Session
  import yfinance as yf
  import time
  from datetime import datetime
  import os

  INDEX_OL = "OLG.PA"
  OPENING = os.getenv("OPENING")
  CLOSING = os.getenv("CLOSING")
  
  oauth = OAuth1Session(
    os.getenv("CONSUMER_KEY"),
    client_secret=os.getenv("CONSUMER_SECRET"),
    resource_owner_key=os.getenv("ACCESS_TOKEN"),
    resource_owner_secret=os.getenv("ACCESS_TOKEN_SECRET"),
  )
  
  def get_value(index,key):
    return yf.Ticker(index).info[key]
    
  def make_tweet_dict(INDEX_OL, OPENING, CLOSING):
    curr_time = time.strftime("%H:%M", time.localtime())
    stock_price = get_value(INDEX_OL,"currentPrice")
    if OPENING:
      date = datetime.today().strftime("%A, %B %d, %Y")
      opening_value = get_value(INDEX_OL,"open")
      tweet_dict = {"text": f"Hello the Gones, today is {date}, the market has opened at {opening_value} and as always fuck Mbuzzcut."}
    elif CLOSING:
      opening_value = get_value(INDEX_OL,"open")
      closing_value = get_value(INDEX_OL,"close")
      percentage_value = round((closing_value - opening_value)/opening_value*100,2)
      if percentage_value>0:
        tweet_dict = {"text": f"Today has been about making easy money with a +{percentage_value}%."}
      elif percentage_value<0:
        tweet_dict = {"text": f"A day to forget like Mbuzzcut's quintuples with a {percentage_value}%."}
      else:
        tweet_dict = {"text": f"A flat day, no more, no less."}
    else:
      tweet_dict = {"text": f"At {curr_time}, OL's current share price is {stock_price}\N{euro sign} and fuck Mbuzzcut."}
    return tweet_dict
  
  def post_tweet(oauth,tweet_dict):
    response = oauth.post("https://api.twitter.com/2/tweets",json=tweet_dict)

  tweet_content = make_tweet_dict(INDEX_OL, OPENING, CLOSING)
  post_tweet(oauth,tweet_content)
