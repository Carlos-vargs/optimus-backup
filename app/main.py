from database.queries import get_all_equipos
from data_processing.data_to_csv import clean_data, transform_data, sort_data, add_headers, export_to_csv
from drive_integration.drive_api import upload_file_to_drive, service_account_login, upload_folder_to_drive


def main():
    # Obtener datos crudos de la base de datos
    raw_data = get_all_equipos()

    # Procesar los datos
    cleaned_data = clean_data(raw_data)
    transformed_data = transform_data(cleaned_data)

    # Ordenar los datos
    sorted_data = sort_data(transformed_data)

    # Añadir encabezados
    data_with_headers = add_headers(sorted_data)

    # Exportar a CSV con la fecha y hora en el nombre del archivo
    export_to_csv(data_with_headers, 'equipos')


if __name__ == "__main__":
    main()
    #creds = service_account_login()
    #folder_path = '../exports'
    # Sube la carpeta completa a Google Drive
    #upload_folder_to_drive(folder_path)
    # upload_file_to_drive('equipos.csv', './exports/equipos.csv', 'text/csv')
