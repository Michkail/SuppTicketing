import boto3

session = boto3.session.Session()
s3_client = session.client(
    's3',
    endpoint_url='http://100.103.184.131:9000',
    aws_access_key_id='1i7RSmBNNmfL7E0V',
    aws_secret_access_key='OyMcsfwxdPSXNgQtxvcZnfG3U7I9hhZ7',
    config=boto3.session.Config(signature_version='s3v4'),
)

# Coba akses objek
response = s3_client.get_object(Bucket='report', Key='your_object_key')
print(response['Body'].read())
