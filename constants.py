import socket
import threading
from Crypto.Cipher import AES
from cripto import *
import time

KEY_MANAGER = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 42069  # Port to listen on (non-privileged ports are > 1023)
HEDER = 64
FORMAT = "utf-8"
DISCONECT_MESSAGE = b"!DC"
DO_NOTHING = b"PIERDE_VREMEA"
START_MESSAGE = b'START'
CHECK_VALUES = b'CHECK_VALUES'
MODE = b"MODE"

MODE_CFB = b"CFB"
MODE_CBC = b"CBC"

K1 = b"AAAABBBBCCCCDDDD"

k1_cipher = AES.new(K1, AES.MODE_ECB)


def read_data(connection):
    """
    Functie folosita pentru a citi datele trimise in retea.
    :param connection:
    :return:
    """
    msg_lenght = connection.recv(HEDER).decode(FORMAT)
    # print(msg_lenght)
    msg_lenght = int(msg_lenght)

    msg = connection.recv(msg_lenght)
    return msg


def write_data(connection, data):
    """
    Functie folosita pentru a trimite datele in retea
    :param connection:
    :param data:
    :return:
    """
    if type(data) == str:
        data = data.encode(FORMAT)
    msg_len = str(len(data)).encode(FORMAT)
    msg_len += b' ' * (HEDER - len(msg_len))
    connection.send(msg_len)
    connection.send(data)


def conn_to_km(km, p):
    """
    Functie utiliata pentru conectarea la key maneger
    :param km:
    :param p:
    :return:
    """
    key_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ADDR = (km, p)
    key_manager.connect(ADDR)
    return key_manager


def setup(key_manager):
    """
    Partea comuna a nodurilor ce se ocupa
    de obtinerea cheii de criptare , vectorului de initializare
    si a modului de operare.
    :param key_manager:
    :return:
    """
    KEY = read_data(key_manager)
    KEY = k1_cipher.decrypt(KEY)
    IV = read_data(key_manager)
    IV = k1_cipher.decrypt(IV)

    mode = read_data(key_manager)
    mode = k1_cipher.decrypt(mode)
    mode = unpadding(mode)
    #print(IV,KEY,mode)
    if mode == MODE_CFB:
        cfe = aes_encrypt_cfb
        cfd = aes_decrypt_cfb
    else:
        cfe = aes_encrypt_cbc
        cfd = aes_decrypt_cbc

    auth_msg = cfe(IV, KEY, IV)
    write_data(key_manager, auth_msg)

    return KEY, IV, mode, cfe, cfd
