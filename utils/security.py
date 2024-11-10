# utils/security.py
import hashlib
import ssl
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        
    def encrypt_data(self, data):
        return self.cipher_suite.encrypt(data.encode())
        
    def decrypt_data(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode()
        
    def validate_certificate(self, cert):
        try:
            context = ssl.create_default_context()
            context.verify_mode = ssl.CERT_REQUIRED
            context.check_hostname = True
            context.load_verify_locations(cafile=cert)
            return True
        except ssl.SSLError:
            return False
            
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
