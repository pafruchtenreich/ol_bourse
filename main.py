if __name__ == "__main__":
  from requests_oauthlib import OAuth1Session
  import yfinance as yf
  import time

  INDEX_OL = "OLG.PA"
  
  oauth = OAuth1Session(
    CONSUMER_KEY,
    client_secret=CONSUMER_SECRET,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_TOKEN_SECRET,
  )
  
  def get_current_price(index):
    return yf.Ticker(index).info["currentPrice"]
    
  def make_tweet_dict(INDEX_OL):
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    stock_price = get_current_price(INDEX_OL)
    tweet_dict = {"text": f"At {curr_time}, OL's current share price is {stock_price}€ and fuck Mbuzzcut."}
    return tweet_dict
  
  def post_tweet(oauth,tweet_dict):
    response = oauth.post("https://api.twitter.com/2/tweets",json=tweet_dict)

  tweet_content = make_tweet_dict(INDEX_OL)
  post_tweet(oauth,tweet_dict)
