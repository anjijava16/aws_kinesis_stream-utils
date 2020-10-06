import os
import json

import boto3
import tweepy

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

access_token = os.getenv("access_token")
access_token_secret =os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

deliveryStreamName="order-stream-firehose"
client = boto3.client('firehose')

class KinesisStreamProducer(tweepy.StreamListener):

    def __init__(self, kinesis_client):
        self.kinesis_client = kinesis_client

    def on_data(self, data):
        tweet = json.loads(data)
        data = json.dumps(tweet)
        response = client.put_record(DeliveryStreamName=deliveryStreamName, Record={'Data': data + '\n'})
        print(response)
        print(str(tweet))
        return True

    def on_error(self, status):
        print("Error: " + str(status))


def main():
    print("main custom method started")
    mylistener = KinesisStreamProducer(client)
    myStream = tweepy.Stream(auth=auth, listener=mylistener)
    myStream.filter(track=['#Trump'])


print("main custom method ended")

if __name__ == "__main__":
    print("main method started")
    main()
    print("main method ended")
