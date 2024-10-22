from werkzeug.security import generate_password_hash, check_password_hash

class Libs:
    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, provided_password, password):
        response = check_password_hash(password, provided_password)
        return response