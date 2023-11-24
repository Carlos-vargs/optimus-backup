from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import os

SCOPES = ['https://www.googleapis.com/auth/drive.file']


def service_account_login():
    return service_account.Credentials.from_service_account_file(
        '/home/carlos/personal/projects/optimus-backup/app/drive_integration/credentials.json', scopes=SCOPES)


def upload_file_to_drive(filename, filepath, mimetype, creds):
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = service.files().create(body=file_metadata,
                                  media_body=media, fields='id').execute()
    print(f"Archivo {filename} ID: {file.get('id')}")


def upload_folder_to_drive(folder_path, creds):
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        drive_file_name = f"exports/{file_name}"
        upload_file_to_drive(drive_file_name, file_path,
                             'application/octet-stream', creds)
