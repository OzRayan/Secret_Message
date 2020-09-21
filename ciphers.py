import string


class Cipher:
    """Cipher parent class
        it has three protected methods + __init__
        __pack method which creates a list of tuples
        Encrypt Method which loops trough the income message,
        identifies the right value from a dict and sends back to the user
        Decrypt Method which loop trough the income encrypted message and sends
        back to the user the identified message"""

    def __init__(self):
        """Constructor"""
        self.alphabet = string.ascii_uppercase

    def pack(self, a, b):
        """pack protected Method, creates a list of tuples"""
        list_ = []
        index = len(self.alphabet)     # Length of the alphabet
        i = 0
        while index:
            list_.append(a[i] + b[i])
            i += 1
            index -= 1      # Making sure that the loop ends
        return list_

    def encrypt_decrypt(self, word, cipher):
        """Encrypting/decrypting method for all the ciphers
            first: loops trough the income message
            second: it checks for the second time that the character is in the cipher key
                    and in the same time makes sure that the char is not whitespace
            third: fills the list with the corresponding value and sends back the encrypted
            or decrypted message """
        output = []
        for char in word.upper():
            if char in cipher.keys():
                output.append(cipher[char])
        return ''.join(output)


class Keyword(Cipher):
    """Keyword child class which inherits from the Main Cipher class
        Sends back to the user the encrypted or decrypted message with a method"""

    def keyword(self, text, key, num):
        """keyword method with the incoming message and the chosen encrypting or decrypting method
            as int value. Sets the cipher to the chosen dict
            Sends back tha main encrypt method which will show the encrypted or decrypted message to the user"""

        need = list(set(self.alphabet) - set(key.upper()))
        key_alphabet = key.upper() + ''.join(sorted(need))
        keyword = self.pack(list(self.alphabet), list(key_alphabet))
        keyword_de = self.pack(list(key_alphabet), list(self.alphabet))
        words = text.split(' ')
        out = []
        if num:
            cipher = dict(keyword)         # Sets cipher to the created dict
        else:
            cipher = dict(keyword_de)
        for word in words:
            out.append(self.encrypt_decrypt(word, cipher))
        return ' '.join(out)


class Atbash(Cipher):
    """Atbash child class which inherits from the Main Cipher class
        Sends back to the user the encrypted or decrypted message with a method"""

    def atbash(self, text, num):
        """atbash method with the incoming message and the chosen encrypting or decrypting method
            as int value. Sets the cipher to the chosen dict
            Sends back tha main encrypt method which will show the encrypted or decrypted message to the user
            uses the __pack method to create a list of tuples"""

        # Encrypting list from alphabet and affine_set list, packing together
        value_co = self.pack(list(self.alphabet), list(reversed(self.alphabet)))
        # Encrypting list from alphabet and affine_set list, packing together inverse order
        value_de = self.pack(list(reversed(self.alphabet)), list(self.alphabet))
        out = []
        words = text.split(' ')
        if num:
            cipher = dict(value_co)     # Sets cipher to the created dict
        else:
            cipher = dict(value_de)     # Sets cipher to the created dict
        for word in words:
            out.append(self.encrypt_decrypt(word, cipher))
        return ' '.join(out)


class Affine(Cipher):
    """Affine child class which inherits from the Main Cipher class
        Sends back to the user the encrypted or decrypted message with a method"""

    def affine(self, text, num):
        """affine method with the incoming message and the chosen encrypting or decrypting method
            as int value. Sets the cipher to the chosen dict
            Sends back tha main encrypt method which will show the encrypted or decrypted message to the user
            uses the __pack method to create a list of tuples"""
        # A string of corresponding english characters and length with alphabet string
        affine_set = 'INSXCHMRWBGLQVAFKPUZEJOTYD'
        # Encrypting list from alphabet and affine_set list, packing together
        value_co = self.pack(list(self.alphabet), list(affine_set))
        # Encrypting list from alphabet and affine_set list, packing together inverse order
        value_de = self.pack(list(affine_set), list(self.alphabet))
        out = []
        words = text.split(' ')
        if num:
            cipher = dict(value_co)  # Sets cipher to the created dict
        else:
            cipher = dict(value_de)  # Sets cipher to the created dict
        for word in words:
            out.append(self.encrypt_decrypt(word, cipher))
        return ' '.join(out)
