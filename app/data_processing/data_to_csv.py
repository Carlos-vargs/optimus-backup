import datetime
import os
import csv


def clean_data(raw_data):
    # Eliminar filas con datos faltantes
    cleaned_data = [row for row in raw_data if None not in row]
    return cleaned_data


def transform_data(cleaned_data):
    transformed_data = [
        (row[0], row[1], row[2], row[3], row[4].strftime('%d/%m/%Y'))
        if isinstance(row[4], datetime.date) else row
        for row in cleaned_data
    ]
    return transformed_data


def sort_data(data):
    sorted_data = sorted(data, key=lambda x: (
        datetime.datetime.strptime(x[4], '%d/%m/%Y'), x[1]))
    return sorted_data


def add_headers(sorted_data):
    headers = ['ID', 'Tipo', 'Marca', 'Estado', 'Fecha de Adquisición']
    return [headers] + sorted_data


def export_to_csv(processed_data, base_file_name):
    output_dir = 'exports'
    os.makedirs(output_dir, exist_ok=True)  # Crea el directorio si no existe

    # Obtén la fecha y hora actual en formato 'año-mes-día_hora-minutos-segundos'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # Construye el nombre del archivo con la fecha y hora
    file_name = f"{base_file_name.split('.')[0]}_{timestamp}.csv"

    file_path = os.path.join(output_dir, file_name)

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(processed_data)
