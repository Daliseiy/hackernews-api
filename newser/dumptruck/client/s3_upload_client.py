import datetime

def upload_json_to_s3(data, file_name, bucket_name):


  import json
  import boto3

  # Get the current date and time
  now = datetime.datetime.now()

  # Get the current month and year
  month = now.strftime("%b")
  year = now.strftime("%Y")

  # Create the dumptruck bucket if it doesn't exist
  s3 = boto3.client("s3")
  if not s3.bucket_exists(bucket_name):
    s3.create_bucket(Bucket=bucket_name)

  # Create the month folder inside the dumptruck bucket
  month_folder = f"{month}_{year}"
  if not s3.object_exists(bucket_name, month_folder):
    s3.put_object(Bucket=bucket_name, Key=month_folder)

  # Create the week folder inside the month folder
  week_folder = f"{now.strftime('%W')}_{year}_{month}"
  if not s3.object_exists(bucket_name, month_folder + "/" + week_folder):
    s3.put_object(Bucket=bucket_name, Key=month_folder + "/" + week_folder)

  # Create the file name
  file_name = "dump_" + now.strftime("%Y-%b-%d_%H-%M-%S")

  # Convert the dict of JSON data to a string
  json_data = json.dumps(data)

  # Upload the file to S3
  s3.put_object(
      Bucket=bucket_name,
      Key=month_folder + "/" + week_folder + "/" + file_name,
      Body=json_data,
  )

  print("File uploaded successfully!")


if __name__ == "__main__":
  # Get the dict of JSON data
  data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
  }

  # Get the file name
  file_name = "dump_" + now.strftime("%Y-%b-%d_%H-%M-%S")

  # Get the bucket name
  bucket_name = "dumptruck"

  # Upload the JSON data to S3
  upload_json_to_s3(data, file_name, bucket_name)
