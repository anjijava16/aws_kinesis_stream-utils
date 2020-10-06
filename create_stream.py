import boto3

client = boto3.client('kinesis')
STREAM_NAME = "order_stream"

def create_stream():
    response = client.create_stream(
        StreamName=STREAM_NAME,
        ShardCount=1
        )
    print(response)


def delete_stream():
    client.delete_stream(StreamName=STREAM_NAME)

def main():
    create_stream()
    #delete_stream()


main()