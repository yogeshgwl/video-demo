import boto3

def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def list_files(bucket):
    s3_client = boto3.client('s3')
    contents = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            contents.append(item)
    except Exception as e:
        pass
    return contents

def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 36000)

            # presigned_url = s3_client.generate_presigned_post(Bucket=bucket,
            #                                          Key="S3KEY",
            #                                          Fields={"Content-Type": "image/jpg"},
            #                                          Conditions=["starts-with", "$Content-Type", "image/"],
            #                                          ExpiresIn=3600)
            # print("[DATA] : presigned url = ", presigned_url)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[DATA] : The contents inside show_image = ", public_urls)
    return public_urls
    
