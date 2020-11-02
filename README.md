SI_TEMA_1



Milea Robert 3B4

Fiecare functie este documentata.

Tema este scris in python 3.8 , pe windows in pycharm.

Daca nu aveti pycryptodome .  pip3 -install pycryptodome

In Powershell-ul pentru nodul A se va introduce modul de operare dorit.


Documentatie : 

NAME
    cripto

FUNCTIONS
    aes_decrypt_cbc(crypto_text, key, initialization_vector)
        Implementare de decriptare AES_CBC .
        :param plaine_text:
        :param key:
        :param initialization_vector:
        :return:
    
    aes_decrypt_cfb(crypto_text, key, initialization_vector)
        Implementare de decriptare AES_CFB .
        :param plaine_text:
        :param key:
        :param initialization_vector:
        :return:
    
    aes_encrypt_cbc(plaine_text, key, initialization_vector)
        Implementare de criptare AES_CBC .
        :param plaine_text:
        :param key:
        :param initialization_vector:
        :return:
    
    aes_encrypt_cfb(plain_text, key, initialization_vector)
        Implementare de criptare AES_CFB .
        :param plaine_text:
        :param key:
        :param initialization_vector:
        :return:
    
    padding(padded_text)
        Functie de padare
        :param padded_text:
        :return:
    
    pp(x)
        Functie ce afiseaza o cheie in hexa.
        :param x:
        :return:
    
    transform(ciphertext)
        Functie auxiliara pentru transformarea unue liste de blocuri
        intr-un mesaj.
        :param ciphertext:
        :return:
    
    unpadding(message)
        Functie care elimina padarea
        :param message:
        :return:

NAME
    constants

FUNCTIONS
    conn_to_km(km, p)
        Functie utiliata pentru conectarea la key maneger
        :param km:
        :param p:
        :return:
    
    read_data(connection)
        Functie folosita pentru a citi datele trimise in retea.
        :param connection:
        :return:
    
    setup(key_manager)
        Partea comuna a nodurilor ce se ocupa
        de obtinerea cheii de criptare , vectorului de initializare
        si a modului de operare.
        :param key_manager:
        :return:
    
    write_data(connection, data)
        Functie folosita pentru a trimite datele in retea
        :param connection:
        :param data:
        :return:

DATA
    CHECK_VALUES = b'CHECK_VALUES'
    DISCONECT_MESSAGE = b'!DC'
    DO_NOTHING = b'PIERDE_VREMEA'
    FORMAT = 'utf-8'
    HEDER = 64
    K1 = b'AAAABBBBCCCCDDDD'
    KEY_MANAGER = '127.0.0.1'
    MODE = b'MODE'
    MODE_CBC = b'CBC'
    MODE_CFB = b'CFB'
    PORT = 6969
    START_MESSAGE = b'START'
    k1_cipher = <Crypto.Cipher._mode_ecb.EcbMode object>


NAME
    key_manager

FUNCTIONS
    check_blocks()
        Functia ce verifica daca blocurile trimise de fiecare nod
        au aceiasi lungime
        :return:
    
    handeler(connection, adrress)
        Functia de ajutor pentru a face thredurile mai usor de folosit,
        Functioneaza ca un meniu pentru clienti
        
        :param connection:
        :param adrress:
        :return:
    
    schimb_de_chei(mode)
        Functia ce realizeaza schibmul de chei
        
        :param mode -- modul de operare dorit:
        :return:
    
    start_serer()
        Functie ce porneste serverul
        :return:

DATA
    CHECK_VALUES = b'CHECK_VALUES'
    DISCONECT_MESSAGE = b'!DC'
    DO_NOTHING = b'PIERDE_VREMEA'
    FORMAT = 'utf-8'
    HEDER = 64
    IV = b'TEMA_DE_10++++++'
    K1 = b'AAAABBBBCCCCDDDD'
    K2 = b'MAMA_ARE_MERE_12'
    K3 = b'TREC_LA_SI_CU_5+'
    KEY_MANAGER = '127.0.0.1'
    MODE = b'MODE'
    MODE_CBC = b'CBC'
    MODE_CFB = b'CFB'
    PORT = 6969
    START_MESSAGE = b'START'
    conexiuni_clienti = []
    k1_cipher = <Crypto.Cipher._mode_ecb.EcbMode object>

