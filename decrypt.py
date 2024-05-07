import string

SECRET_FILENAME = "secret.txt"
DECRYPTED_FILENAME = "final.txt"
DEFAULT_KEY = 13

class Decrypt:
    def __init__(self):
        self.ciphertext : str = ""
        self.key : int

    def getKey(self, key:int=DEFAULT_KEY) -> None:
        if key > 25 or key < 1:
            raise ValueError("key should be an integer in the range 1-25")
        else:
            self.key = key

    def getText(self, secret_file:str=SECRET_FILENAME, show_ciphertext:bool=False) -> None: 
        with open(secret_file, "r") as f:
            self.ciphertext = f.read()
        if show_ciphertext:
            print(self.ciphertext)
        else:
            print("show_ciphertext parameter is set to false")

    def decipherMessage(self, cleartext_file:str=DECRYPTED_FILENAME, show_cleartext:bool=False) -> None:
        """
        the assignment is unclear but I'm guessing this must be a ROT13 algorithm
        """
        cleartext = ""
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        k = self.key
        # make a translation function that shifts characters by 'k' indexes
        translation_table = str.maketrans(lc+uc, (lc[k:] + lc[:k] + uc[k:] + uc[:k]))
        cleartext = str.translate(self.ciphertext, translation_table)
        if show_cleartext:
            print(f"Deciphered Message:\n{cleartext}")
        else:
            print("not printing deciphered message because show_cleartext is False")
        with open(cleartext_file, "w+") as f:
            f.write(cleartext)
