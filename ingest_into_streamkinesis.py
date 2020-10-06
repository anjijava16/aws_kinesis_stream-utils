from faker import Faker
from faker.providers import internet
from random import random
from random import randrange
import time
import json
import datetime
import boto3


fake = Faker()
deliveryStreamName="order_stream"
client = boto3.client('kinesis')

def main():
    record={}
    i=1
    while True:
        record['User']=fake.name()
        record['OrderId']=i
        record['ProductId']=randrange(1,5000)
        record['StoreId']=randrange(1,5000)
        record['InvoiceTime']=time.ctime(time.time())
        record['units']=randrange(1,100)
        record['amt']=randrange(1,1000)
        i=i+1
        data=json.dumps(record)
        response=client.put_record(StreamName=deliveryStreamName,
                                   Data=data,
                                   PartitionKey=str(i))
        print(data)


main()