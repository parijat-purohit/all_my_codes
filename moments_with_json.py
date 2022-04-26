from urllib.request import urlopen

ACCESS_KEY =''
SECRET_ACCESS_KEY = ''

# Read from file
with open('sample.json') as f:
    data1 = json.load(f)
print(data1)


# Read from an URL
your_url=""
with urlopen(your_url) as response:
    data = response.read()

data = json.loads(data)
for d in data:
    print(data[d])


# read json from aws bucket
client = boto3.client('s3',
                      aws_access_key_id= ACCESS_KEY,
                      aws_secret_access_key=SECRET_ACCESS_KEY)
response = client.get_object(Bucket='parijatjson' , Key='sample2.json')
data2 = json.loads(response['Body'].read())

data3 = {}
for d in data2['users']:
    if d['userId'] in data1['id']: #we are comparing some keys in our json files
        print(d)
        # output a json file in the s3 bucket
        response = client.put_object(Body=json.dumps(d), Bucket='parijatjson',
                                     Key='{}.json'.format(d['userId']))
