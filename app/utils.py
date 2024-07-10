from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def hash(password):
    return pwd_context.hash(password)