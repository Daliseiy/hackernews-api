import datetime

def upload_json_to_google_drive(data, file_name):
  """Uploads a dict of JSON data to Google Drive as a JSON file.

  Args:
    data: The dict of JSON data to upload.
    file_name: The name of the file to upload.

  Returns:
    None.
  """

  import json
  from google.colab import drive

  # Authenticate with Google Drive
  drive.mount("drive")

  # Get the current date and time
  now = datetime.datetime.now()

  # Get the current month and year
  month = now.strftime("%b")
  year = now.strftime("%Y")

  # Create the dumptruck folder if it doesn't exist
  dumptruck_folder = drive.CreateFolder("dumptruck")

  # Create the month folder if it doesn't exist
  month_folder = drive.CreateFolder(f"{month}_{year}")

  # Create the week folder
  week_folder = drive.CreateFolder(f"{month}_{now.strftime('%W')}_{year}")

  # Create the file name
  file_name = "dump_" + now.strftime("%Y-%b-%d_%H-%M-%S")

  # Convert the dict of JSON data to a string
  json_data = json.dumps(data)

  # Write the JSON data to the file
  file = drive.CreateFile({"name": file_name})
  file.setContent(json_data)

  # Upload the file to Google Drive
  file.Upload()

  # Move the file to the week folder
  file.Move(week_folder)

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

  # Upload the JSON data to Google Drive
  upload_json_to_google_drive(data, file_name)
