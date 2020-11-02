from constants import *
from cripto import *
if __name__ == "__main__":
    # Conectarea la KM
    print("NODE A:")
    key_manager = conn_to_km(KEY_MANAGER, PORT)

    write_data(key_manager, MODE)
    if input("ALEGE MODUL DE CRIPTARE  (CBC/CFB) =").upper() == MODE_CFB.decode('ascii'):
        write_data(key_manager, MODE_CFB)
    else:
        write_data(key_manager, MODE_CBC)

    # write_data(key_manager, MODE_CFB)

    KEY, IV, mode, cfe, cfd = setup(key_manager)

    if read_data(key_manager) == START_MESSAGE:
        key_manager.shutdown(socket.SHUT_WR)
        key_manager.close()

        text = open(input("Path fisier (./node_a.py): "), "rb").read()
        crypo_text = cfe(text, KEY, IV)

        # print(cfd(cripo_text, KEY, IV).decode("ascii"))

        send_to_b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (KEY_MANAGER, PORT + 2)
        send_to_b.connect(ADDR)
        write_data(send_to_b, crypo_text)
        send_to_b.close()

        key_manager = conn_to_km(KEY_MANAGER, PORT)

        write_data(key_manager, DO_NOTHING)
        write_data(key_manager, bytes(len(crypo_text)//128))


    print("Transfer finalizat.")
    key_manager.shutdown(socket.SHUT_WR)
    key_manager.close()
