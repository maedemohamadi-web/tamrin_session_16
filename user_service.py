from user_data_manager import UserDataAccess

class UserService:
    def __init__(self):
        self.__data_access = UserDataAccess()

    def save(self, user):
        if not self.__data_access.is_unique(user.the_national_id,user.the_phone_number):
            return False, "Error,national id or phone number already exists"

        if self.__data_access.save(user):
             return True, "saved successfully"
        return False, "save failed"


    def edit(self, user):
        # todo : کدملی و شماره تلفن منحصر به فرد
        print(" غیر تکراری")
        self.__data_access.edit(user)

    def delete(self, the_national_id):
        self.__data_access.delete(the_national_id)

    def get_all(self):
        return self.__data_access.get_all()

    def get_by_national_id(self, the_national_id):
        return self.__data_access.get_by_national_id(the_national_id)
