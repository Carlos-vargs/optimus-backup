from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
import os.path
import pickle


# elimina el archivo token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']


def service_account_login():
    creds = None
    # El archivo token.pickle almacena los tokens de acceso y actualización del usuario, y se
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si no hay credenciales disponibles o si las credenciales son inválidas, haz que el usuario se loguee.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para la próxima ejecución
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def upload_file_to_drive(filename, filepath, mimetype):
    creds = service_account_login()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)

    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()

    print(f"Archivo {filename} ID: {file.get('id')}")


def upload_folder_to_drive(folder_path):
    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        drive_file_name = f"exports/{file_name}"
        upload_file_to_drive(drive_file_name, file_path,
                             'application/octet-stream')
