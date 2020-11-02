# SI_TEMA_1

## Milea Robert 3B4

### Fiecare functie este documentata.

### Tema este scrisa in python 3.8 , pe windows in pycharm.

### Daca nu aveti pycryptodome  pip3 -install pycryptodome

### In Powershell-ul pentru nodul A se va introduce modul de operare dorit.

Ordinea de rulare este KM , Nod B , Nod A .

De preferat este sa rulati RUN.bat

### Comunicarea intre KM , Nod A , Nod B:
Km joaca rol de server.
Nod A si Nod B se vor conecta.
Nod A trimite o comanda pentru a initializa transferul de data .
KM rapsunde cu cheia , vectorul de initializare si modul de operare 
si inchide conexiunea cu cei 2.

Nodul B isi deschide un port si asteapta sa primeasca mesajul criptat.
Nodul A cripteaza un fisier cu pathul citit de la tastatura si il trimite
nodului B.

Nodul A se reconecteaza la server si trimite numarul de blocuri transmise
lui B
Nodul B se reconecteaza la server , trimie o comanda pentru a incepe verificarea
si trimite numarul de blocuri primite de la nodul A

Daca totul este OK  , nodul KM afiseaza mesajul "Totul este bine! Transfer realizat cu succes"

### Documentatie :     

``` py
    NAME
    key_manager

FUNCTIONS
    check_blocks()
    
    handeler(connection, adrress)
        Functia de ajutor pentru a face thredurile mai usor de folosit,
        Functioneaza ca un meniu pentru clienti
        
        :param connection:
        :param adrress:
        :return None:
    
    schimb_de_chei(mode)
        Functia ce realizeaza schibmul de chei
        
        :param mode -- modul de operare dorit:
        :return None:
    
    start_serer()
        Functie ce porneste serverul
        :return None:

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
    ON = True
    PORT = 42069
    START_MESSAGE = b'START'
    conexiuni_clienti = []
    k1_cipher = <Crypto.Cipher._mode_ecb.EcbMode object>
```

   
``` py
    NAME
    cripto

FUNCTIONS
    aes_decrypt_cbc(crypto_text, key, initialization_vector)
        Implementare de decriptare AES_CBC .
        Implementare dupa modelul prezentat la seminar.
        :param crypto_text:
        :param key:
        :param initialization_vector:
        :return  O lista de biti ce reprezinta crypto textul decriptat. :
    
    aes_decrypt_cfb(crypto_text, key, initialization_vector)
        Implementare de decriptare AES_CFB .
        Implementare dupa modelul prezentat la seminar.
        :param crypto_text:
        :param key:
        :param initialization_vector:
        :return O lista de biti ce reprezinta crypto textul decriptat.:
    
    aes_encrypt_cbc(plaine_text, key, initialization_vector)
        Implementare de criptare AES_CBC .
        Implementare dupa modelul prezentat la seminar.
        :param plaine_text:
        :param key:
        :param initialization_vector:
        :return O lista de biti ce reprezinta  textul criptat.:
    
    aes_encrypt_cfb(plain_text, key, initialization_vector)
        Implementare de criptare AES_CFB .
        Implementare dupa modelul prezentat la seminar.
        :param plaine_text:
        :param key:
        :param initialization_vector:
        :return  O lista de biti ce reprezinta  textul criptat.:
    
    padding(padded_text)
        Functie de padare
        :param padded_text:
        :return O lista de biti ce repezinta textul padat: 
    
    pp(x)
        Functie ce afiseaza o cheie in hexa.
        :param x:
        :return:
    
    transform(ciphertext)
        Functie auxiliara pentru transformarea unue liste de blocuri
        intr-un mesaj.
        :param ciphertext:
        :return Bytes:
    
    unpadding(message)
        Functie care elimina padarea
        :param message:
        :return  O lista de biti ce repezinta textul fara padare:

```

    

``` py
NAME
    constants

FUNCTIONS
    conn_to_km(km, p)
        Functie utiliata pentru conectarea la key maneger
        :param km:
        :param p:
        :return socket.socket:
    
    read_data(connection)
        Functie folosita pentru a citi datele trimise in retea.
        :param connection:
        :return bytes:
    
    setup(key_manager)
        Partea comuna a nodurilor ce se ocupa
        de obtinerea cheii de criptare , vectorului de initializare
        si a modului de operare.
        :param key_manager:
        :return cheia, vectorul de initializare, modeul de utilizare, functia de criptare, functia de decriptare:
    
    write_data(connection, data)
        Functie folosita pentru a trimite datele in retea
        :param connection:
        :param data:
        :return None:

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
    PORT = 42069
    START_MESSAGE = b'START'
    k1_cipher = <Crypto.Cipher._mode_ecb.EcbMode object>

    ```
