from werkzeug.security import generate_password_hash, check_password_hash

class Libs:
    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, old_password, password):
        return check_password_hash(old_password, password)