from constants import *

if __name__ == "__main__":
    # Conectarea la KM
    print("NODE B:")
    key_manager = conn_to_km(KEY_MANAGER, PORT)

    write_data(key_manager, DO_NOTHING)

    KEY, IV, mode, cfe, cfd = setup(key_manager)

    print("Modul selectat de nodul a este ", mode)

    if read_data(key_manager) == START_MESSAGE:
        key_manager.shutdown(socket.SHUT_WR)
        key_manager.close()
        # B asteapta  mesaje de la A
        node_b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        node_b.bind((KEY_MANAGER, PORT + 2))
        node_b.listen(1)
        connection, address = node_b.accept()

        crypto_text = read_data(connection)

        node_b.close()

        key_manager = conn_to_km(KEY_MANAGER, PORT)

        write_data(key_manager, CHECK_VALUES)
        write_data(key_manager, bytes(len(crypto_text)//128))

        plain_text = cfd(crypto_text, KEY, IV).decode("ascii")

        print(plain_text)

        # print(cfd(cripo_text, KEY, IV).decode("ascii"))

    print("TRANSFER FINALIZAT")
    key_manager.shutdown(socket.SHUT_WR)
    key_manager.close()
