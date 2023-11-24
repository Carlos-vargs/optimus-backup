from database.queries import get_all_equipos


def main():
    equipos = get_all_equipos()
    print(equipos)


if __name__ == "__main__":
    main()
