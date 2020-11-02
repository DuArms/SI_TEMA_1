from constants import *
from cripto import *
import sys
conexiuni_clienti = []

K2 = b"MAMA_ARE_MERE_12"
K3 = b"TREC_LA_SI_CU_5+"
IV = b"TEMA_DE_10++++++"

ON = True


def schimb_de_chei(mode):
    """
    Functia ce realizeaza schibmul de chei

    :param mode -- modul de operare dorit:
    :return:
    """
    global conexiuni_clienti
    if mode == MODE_CBC:
        key_to_be_sent = k1_cipher.encrypt(bytes(K2))
        crypto_functio = aes_decrypt_cbc
    else:  # mode == MODE_CFB:
        key_to_be_sent = k1_cipher.encrypt(bytes(K3))
        crypto_functio = aes_decrypt_cfb

    for conn in conexiuni_clienti:
        write_data(conn, key_to_be_sent)
        write_data(conn, k1_cipher.encrypt(bytes(IV)))
        write_data(conn,  k1_cipher.encrypt(padding(mode)))

    expected_response = IV
    print(IV)
    for conn in conexiuni_clienti:
        msg = read_data(conn)
        print(msg)
        if crypto_functio(msg, k1_cipher.decrypt(key_to_be_sent), IV) != bytes(expected_response):
            raise ValueError("Cheie criptata incorect")

    print("Check e ok")

    for conn in conexiuni_clienti:
        write_data(conn, START_MESSAGE)
        time.sleep(0.001)
        conn.shutdown(socket.SHUT_WR)
        conn.close()

    conexiuni_clienti = []


def check_blocks():
    """
    Functia ce verifica daca blocurile trimise de fiecare nod
    au aceiasi lungime
    :return:
    """
    global conexiuni_clienti
    while len(conexiuni_clienti) == 1:
        time.sleep(0.001)
    values = []
    for conn in conexiuni_clienti:
        values.append(read_data(conn))
        conn.shutdown(socket.SHUT_WR)
        conn.close()
    conexiuni_clienti = []

    if values.count(values[0]) != len(values):
        raise ValueError("Ceva nu a mers bine")

    print("Totul este bine! Transfer realizat cu succes")


def handeler(connection, adrress):
    """
    Functia de ajutor pentru a face thredurile mai usor de folosit,
    Functioneaza ca un meniu pentru clienti

    :param connection:
    :param adrress:
    :return:
    """
    comanda = read_data(connection)
    if comanda == DISCONECT_MESSAGE:
        connection.close()
    elif comanda == MODE:
        schimb_de_chei(read_data(connection))
    elif comanda == CHECK_VALUES:
        check_blocks()
    elif comanda == DO_NOTHING:
        return


def start_serer():
    """
    Functie ce porneste serverul
    :return:
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((KEY_MANAGER, PORT))

    print(f"[ LISTENING ] : {KEY_MANAGER}:{PORT}")

    server.listen(5)

    while ON:
        print("[ SERVER ] Server is UP")
        connection, address = server.accept()
        conexiuni_clienti.append(connection)
        new_thread = threading.Thread(
            target=handeler, args=(connection, address))
        #new_thread.demon = True
        new_thread.start()
        print("[ SERVER ] : S-a conectat ", address)

    server.close()


if __name__ == "__main__":
    print("KEY MANEGER :")
    start_serer()
