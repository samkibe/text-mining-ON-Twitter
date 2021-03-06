from typing import Text
from requests.models import Response
import tweepy
import matplotlib.pyplot as plt
import requests
import os
import json
import numpy as np
import sys
import csv
from twarc_csv import CSVConverter
import sys

#uncomment any code to test.

# Create these keys and tokens in your Twitter Developer account check #readme


consumer_key = "#"
consumer_secret = "#"
bearer_token = "#"
Access_token = "#"
Access_token_secret = "#"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_secret, consumer_key)

# Setting your access token and secret
auth.set_access_token(Access_token,Access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 


search_url = "https://api.twitter.com/2/tweets/search/recent?"
#query_params = {  'query': '#Alshabaab (Alshabaab OR shabaab OR Jihad OR Mujahidin OR mandera OR wajir -is:retweet) OR #Garrissa ', 
#'tweet.fields':   'author_id', }
query_params = {  'query': '#Alshabaab (Alshabaab OR shabaab OR Jihad OR Mujahidin OR mandera OR wajir -is:retweet) OR #Garrissa ', 
'tweet.fields':   'author_id'}

#"expansions": "entities.mentions.username"
#'tweet.fields': 'author_id'
#cool stuff
#'tweet.fields': 'lang',
#'tweet.fields': 'source',
#'tweet.fields':'referenced_tweets'

#[{"parameters":{"expansions":["username"]},"message":"The `expansions` query parameter value [username] is not one of [author_id,referenced_tweets.id,referenced_tweets.id.author_id,entities.mentions.username,attachments.poll_ids,attachments.media_keys,in_reply_to_user_id,geo.place_id]"}],


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()



def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
   # print(json.dumps(json_response, indent=4, sort_keys=True))
#output_file = json.dumps
  
    with open("Search.json", "w") as f:
     json.dump(json_response, f, indent=4, sort_keys=True)



#for page in query_params:
    # Do something with the page of results:
 #   with open("Search.json", "w+", encoding="utf8") as f:
  #     f.write(json.dumps(page) + "\n")   



#with open("Search.json", "r",encoding="utf8") as infile:
 #with open("Search.csv", "w",encoding="utf8") as outfile :
  #   converter = CSVConverter(infile = infile,
   #  outfile = outfile,
    #   json_encode_all=False, 
     # json_encode_lists=True,
      # json_encode_text=False,
      #  inline_referenced_tweets=True, 
       # allow_duplicates=False, 
       # batch_size=100,
        #output_columns="id,text,created_at,author_id")



if __name__ == "__main__":
   main()
   print("Finished crawling, saving json-file.")
