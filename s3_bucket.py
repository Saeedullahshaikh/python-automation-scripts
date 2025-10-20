import boto3
from pathlib import Path

def connect_s3():

    try:
        s3 = boto3.resource('s3')
        print(" Successfully connected to AWS s3 bucket")
        return s3
    except Exception as e:
        print(f" Could not connect to S3: {e}")
        return None


def list_buckets(s3):

    print("\n Your S3 Buckets:")
    try:
        buckets = list(s3.buckets.all())
        if not buckets:
            print("No buckets found in your account.")
            return []
        
        for idx, bucket in enumerate(buckets, 1):
            print(f"{idx}. {bucket.name}")
        return [bucket.name for bucket in buckets]

    except Exception as e:
        print(f" Error while listing buckets: {e}")
        return []


def upload_file(s3, file_path, bucket_name, key_name):

    file_path_obj = Path(file_path)
    if not file_path_obj.is_file():
        print(f" File '{file_path}' does not exist.")
        return False

    try:
        with open(file_path, 'rb') as data:
            s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
        print(f" File '{file_path}' uploaded successfully to '{bucket_name}/{key_name}'!")
        return True
    except Exception as e:
        print(f" Failed to upload file: {e}")
        return False


def download_file(s3, bucket_name, key_name, save_as):

    try:
        s3.Bucket(bucket_name).download_file(key_name, save_as)
        print(f" File '{key_name}' from bucket '{bucket_name}' downloaded successfully as '{save_as}'!")
        return True
    except Exception as e:
        print(f" Failed to download file: {e}")
        return False
