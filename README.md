# aws_kinesis_stream-utils
aws_kinesis_stream_utils

## Github 
https://github.com/neocortex/twitter-stream
https://nicovibert.com/2019/07/30/twitter-apis-python-dynamodb/
https://github.com/theemadnes/iot_anomaly_analytics

Kinesis family of Products

i.   AWS Kinesis Data Streams
ii.  AWS Kinesis Data Firehouse
iii. AWS Kinesis Data Analytics
iv.  AWS kinesis Video

# Project 1:
 
 Custom Python Code to generate push data ---> AWS EC2 ---> Point of Sale Steaming data ---> Kinesis Firehouse ----> Point of Sale Real time data analaytics
                                                                                                       |
																									   |   ---> S3 ----> S3 Data lake
																									   
# Project 1:
Roles --->POSAnalyticsRole ---> AWS Services :kinesis Anlaystics
          POSEc2Role ---> ec2
          POSEFirehouseRole ---> firehouse
          POSELambdaRole ---> lambda
          		  


#  Project 2:
 
 Custom Python Code --> EC2 ---> Kinesis Stream --> Lambda Functopm --_> Amazon DynamoDB ---> Amazon RedShift ---> Analytics /Reporting
                                        |--> Lambda ---> SNS ---->Alert to Phone 


ROles:
   AWSLamdbaFullAccess
   AWSKinesisFullAccess 
   
 sud su 
yum install aws-kinesis-agent -y
cd /etc/aws-kinesis
ls -ltr 
agent.d ,agents.json ,log4j.xml 

vi agents.json (acccess Key,secury key, KineissStream OISDataStream) and dataprocessingOptions:[


 

## POS Flow 

POS Data ---> POS Stream ----> DynamoDB Ingest Function ----> POS RealtimeData ----> Analytics / Reporting 

{"User": "Lori Curry", "OrderId": 1, "ProductId": 1711, "StoreId": 4568, "InvoiceTime": "Mon Oct  5 14:17:53 2020", "units": 49, "amt": 187}


Creating Firehose Stream in :

S3 Output Partitions Example :

# Prefix Path ::
    orderjson/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:hh}/
# Error Prefix Path ::
     ordertwitterjsonFailures/!{firehose:error-output-type}/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:hh}/

    {"ticker_symbol":"QXZ", "sector":"HEALTHCARE", "change":-0.05, "price":84.51}

## Direct table creation Path ::

```
CREATE EXTERNAL TABLE orderjson (
User string ,
OrderId string ,
ProductId string ,
StoreId string ,
InvoiceTime string ,
units string ,
amt string )
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://order-stream-firehose/json/2020/10/05/18/';

```
## Partition Table 

```
CREATE EXTERNAL TABLE orderpartitiontbl (
User string ,
OrderId string ,
ProductId string ,
StoreId string ,
InvoiceTime string ,
units string ,
amt string )
PARTITIONED BY (
year string,
month string,
day string,
hour string)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://order-stream-firehose/orderjson';

```

# msck repair table orderpartitiontbl;


### UseCase 2::
 # Twitter ---> Kinesis Stream ---> Kinesis Firehose ---> S3 ---> Athena 

## External TBL 

```

CREATE EXTERNAL TABLE `kinesis_stream.twitter`(
  `created_at` string COMMENT 'from deserializer', 
  `id` string COMMENT 'from deserializer', 
  `id_str` string COMMENT 'from deserializer', 
  `text` string COMMENT 'from deserializer', 
  `display_text_range` array<string> COMMENT 'from deserializer', 
  `source` string COMMENT 'from deserializer', 
  `truncated` string COMMENT 'from deserializer', 
  `user` struct<id:string,id_str:string,name:string,screen_name:string,location:string,description:string,protected:string,verified:string,followers_count:string,friends_count:string,listed_count:string,favourites_count:string,statuses_count:string,created_at:string,utc_offset:string,time_zone:string,geo_enabled:string,lang:string> COMMENT 'from deserializer', 
  `is_quote_status` string COMMENT 'from deserializer', 
  `extended_tweet` struct<full_text:string,display_text_range:array<string>,entities:struct<media:array<struct<id:string,id_str:string,indices:array<string>,media_url:string,media_url_https:string,url:string,display_url:string,expanded_url:string,type:string,sizes:struct<small:struct<w:string,h:string,resize:string>,thumb:struct<w:string,h:string,resize:string>>>>>> COMMENT 'from deserializer', 
  `retweet_count` string COMMENT 'from deserializer', 
  `favorite_count` string COMMENT 'from deserializer', 
  `retweeted_status` struct<retweet_count:string,text:string> COMMENT 'from deserializer', 
  `entities` struct<urls:array<struct<expanded_url:string>>,user_mentions:array<struct<screen_name:string,name:string>>,hashtags:array<struct<text:string>>> COMMENT 'from deserializer', 
  `favorited` string COMMENT 'from deserializer', 
  `retweeted` string COMMENT 'from deserializer', 
  `possibly_sensitive` string COMMENT 'from deserializer', 
  `filter_level` string COMMENT 'from deserializer', 
  `lang` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://order-stream-error-firehouse/'
TBLPROPERTIES ('transient_lastDdlTime'='1601947941')

```


https://github.com/neocortex/twitter-stream
https://nicovibert.com/2019/07/30/twitter-apis-python-dynamodb/
https://github.com/theemadnes/iot_anomaly_analytics


# ordertwitterinputjson Partition Table 


```


CREATE EXTERNAL TABLE `kinesis_stream.ordertwitter`(
  `created_at` string COMMENT 'from deserializer', 
  `id` string COMMENT 'from deserializer', 
  `id_str` string COMMENT 'from deserializer', 
  `text` string COMMENT 'from deserializer', 
  `display_text_range` array<string> COMMENT 'from deserializer', 
  `source` string COMMENT 'from deserializer', 
  `truncated` string COMMENT 'from deserializer', 
  `user` struct<id:string,id_str:string,name:string,screen_name:string,location:string,description:string,protected:string,verified:string,followers_count:string,friends_count:string,listed_count:string,favourites_count:string,statuses_count:string,created_at:string,utc_offset:string,time_zone:string,geo_enabled:string,lang:string> COMMENT 'from deserializer', 
  `is_quote_status` string COMMENT 'from deserializer', 
  `extended_tweet` struct<full_text:string,display_text_range:array<string>,entities:struct<media:array<struct<id:string,id_str:string,indices:array<string>,media_url:string,media_url_https:string,url:string,display_url:string,expanded_url:string,type:string,sizes:struct<small:struct<w:string,h:string,resize:string>,thumb:struct<w:string,h:string,resize:string>>>>>> COMMENT 'from deserializer', 
  `retweet_count` string COMMENT 'from deserializer', 
  `favorite_count` string COMMENT 'from deserializer', 
  `retweeted_status` struct<retweet_count:string,text:string> COMMENT 'from deserializer', 
  `entities` struct<urls:array<struct<expanded_url:string>>,user_mentions:array<struct<screen_name:string,name:string>>,hashtags:array<struct<text:string>>> COMMENT 'from deserializer', 
  `favorited` string COMMENT 'from deserializer', 
  `retweeted` string COMMENT 'from deserializer', 
  `possibly_sensitive` string COMMENT 'from deserializer', 
  `filter_level` string COMMENT 'from deserializer', 
  `lang` string COMMENT 'from deserializer')
PARTITIONED BY (
year string,
month string,
day string,
hour string)
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://order-stream-firehose/ordertwitterinputjson/'
TBLPROPERTIES ('transient_lastDdlTime'='1601947941')
  

```

