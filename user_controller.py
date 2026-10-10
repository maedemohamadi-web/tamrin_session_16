from datetime import datetime

from user import User
from user_service import UserService
class UserController:
    def __init__(self):
        self.__service = UserService()

    def save(self,name, family, the_national_id, birth_date, the_phone_number, user_name, password, role):
        try:
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
            user = User(name, family, the_national_id, birth_date, the_phone_number, user_name, password, role)
            self.__service.save(user)
            return True, f"Info : {user} Saved"
        except Exception as e:
            return False, f"Error : {e}"

    def edit(self, name, family, the_national_id, birth_date, the_phone_number, user_name, password, role):
        try:
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
            user = User(name, family, the_national_id, birth_date, the_phone_number, user_name, password, role)
            self.__service.edit(user)
            return True, f"Info : {user} Edited"
        except Exception as e:
            return False, f"Error : {e}"

    def delete(self, the_national_id):
        try:

            self.__service.delete(the_national_id)
            return True, f"Info : {the_national_id} Deleted"
        except Exception as e:
            return False, f"Error : {e}"

    def get_all(self):
        try:
            users = self.__service.get_all()
            return True, users
        except Exception as e:
            return False, f"Error : {e}"

    def get_by_national_id(self, the_national_id):
        try:
            users = self.__service.get_by_national_id(the_national_id)
            return True, users
        except Exception as e:
            return False, f"Error : {e}"