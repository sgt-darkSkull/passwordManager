import hashlib
from api.database import user_db
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa


class Authentication:

    def __init__(self):
        self.creds = None
        self.input_password = ""
        self.username = ""

    def get_passwd_hash(self):
        return hashlib.sha512(self.input_password.encode()).hexdigest()

    def user_auth_verification(self):
        db = user_db.UserDataBase()
        db.unlock_database()
        self.creds = db.get_credentials(self.username)
