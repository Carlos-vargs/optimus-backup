from .db_connection import create_db_connection


def get_all_equipos():
    connection = create_db_connection()
    query = """
    SELECT e.id, te.nombre AS tipo_equipo, m.nombre AS marca, es.nombre AS estado, e.fechaDeAdquisicion
    FROM equipos e
    JOIN tipo_equipos te ON e.idTipoEquipo = te.id
    JOIN marcas m ON e.idMarca = m.id
    JOIN estados es ON e.idEstado = es.id;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    connection.close()
    return result
