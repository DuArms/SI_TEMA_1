from Crypto.Cipher import AES


def pp(x):
    """
    Functie ce afiseaza o cheie in hexa.
    :param x:
    :return:
    """
    for a in x:
        print("{:02X}".format(a), end=" ")
    print()


def transform(ciphertext):
    """
    Functie auxiliara pentru transformarea unue liste de blocuri
    intr-un mesaj.
    :param ciphertext:
    :return:
    """
    aux = []
    for ct in ciphertext:
        for c in ct:
            aux.append(c)

    return bytes(aux)


def padding(padded_text):
    """
    Functie de padare
    :param padded_text:
    :return:
    """
    byte_to_add = 16 - (len(padded_text) % 16)

    if type(padded_text) == str:
        return bytes(padded_text, 'ascii') + bytes([byte_to_add]) * byte_to_add
    return bytes(padded_text) + bytes([byte_to_add]) * byte_to_add


def unpadding(message):
    """
    Functie care elimina padarea
    :param message:
    :return:
    """
    if message[-1] <= 16:
        if (message[- message[-1]]) == message[-1]:
            message = message[:-message[-1]]
    return message


def aes_encrypt_cbc(plaine_text, key, initialization_vector):
    """
    Implementare de criptare AES_CBC .
    :param plaine_text:
    :param key:
    :param initialization_vector:
    :return:
    """
    plaine_text = padding(plaine_text)
    initialization_vector = padding(initialization_vector)

    cipher_ecb = AES.new(key, AES.MODE_ECB)

    ciphertext = []

    for i in range(0, len(plaine_text), 16):
        block_of_text = list(plaine_text[i:i + 16])

        for ii in range(16):
            block_of_text[ii] = block_of_text[ii] ^ initialization_vector[ii]

        block_of_text = cipher_ecb.encrypt(bytes(block_of_text))
        initialization_vector = block_of_text
        ciphertext.append(block_of_text)

    return transform(ciphertext)


def aes_decrypt_cbc(crypto_text, key, initialization_vector):
    """
    Implementare de decriptare AES_CBC .
    :param plaine_text:
    :param key:
    :param initialization_vector:
    :return:
    """
    cipher_ecb = AES.new(key, AES.MODE_ECB)

    ciphertext = []

    for i in range(0, len(crypto_text), 16):
        block_of_text = list(crypto_text[i:i + 16])
        next_iv = list(crypto_text[i:i + 16])
        dct = cipher_ecb.decrypt(bytes(block_of_text))

        for ii in range(16):
            block_of_text[ii] = dct[ii] ^ initialization_vector[ii]

        initialization_vector = next_iv
        ciphertext.append(block_of_text)

    padded_text = transform(ciphertext)

    return unpadding(padded_text)


def aes_encrypt_cfb(plain_text, key, initialization_vector):
    """
    Implementare de criptare AES_CFB .
    :param plaine_text:
    :param key:
    :param initialization_vector:
    :return:
    """
    plain_text = padding(plain_text)
    initialization_vector = padding(initialization_vector)

    cipher_ecb = AES.new(bytes(key), AES.MODE_ECB)

    ciphertext = []

    for i in range(0, len(plain_text), 16):
        block_of_text = list(plain_text[i:i + 16])

        initialization_vector = cipher_ecb.encrypt(bytes(initialization_vector))
        for ii in range(16):
            block_of_text[ii] = block_of_text[ii] ^ initialization_vector[ii]

        initialization_vector = block_of_text
        ciphertext.append(block_of_text)

    return transform(ciphertext)


def aes_decrypt_cfb(crypto_text, key, initialization_vector):
    """
    Implementare de decriptare AES_CFB .
    :param plaine_text:
    :param key:
    :param initialization_vector:
    :return:
    """
    cipher_ecb = AES.new(bytes(key), AES.MODE_ECB)

    plaintext = []

    for i in range(0, len(crypto_text), 16):
        block_of_text = list(crypto_text[i:i + 16])
        save = list(crypto_text[i:i + 16])
        initialization_vector = cipher_ecb.encrypt(bytes(initialization_vector))
        for ii in range(16):
            block_of_text[ii] = block_of_text[ii] ^ initialization_vector[ii]

        initialization_vector = save
        plaintext.append(block_of_text)

    return unpadding(transform(plaintext))


if __name__ == "__main__":
    K2 = b"TATA_ARE_PERE_77"

    iv = b"A" * 16  # padare( "A" * 16)
    text = b"0123456789ABCDEF" * 10

    rez_meu = aes_encrypt_cfb(text, K2, iv)

    cipher = AES.new(bytes(K2), AES.MODE_CFB, iv, segment_size=128)

    rez_python = cipher.encrypt(padding(text))

    rd = aes_decrypt_cfb(rez_meu, K2, iv)

    pp(rd)
    pp(rez_python)
    print(rez_meu == rez_python)

    print(text)
    print(rd)
    print(text == rd)
