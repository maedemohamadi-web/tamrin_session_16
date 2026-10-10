class UserDataAccess:
    def __init__(self):
        self.__user_list = []

    def is_unique(self, the_national_id,the_phone_number):
        for user in self.__user_list:
            if user.national_id == the_national_id or user.phone_number == the_phone_number:
                return False
        return True

    def save(self, user):
        if self.is_unique(user.the_national_id,user.the_phone_number):
            self.__user_list.append(user)
            return True
        return False


    def edit(self, user):
        print("EDIT :", user)

    def delete(self, the_national_id):
        print("DELETE :", the_national_id)

    def get_all(self):
        return self.__user_list.copy()

    def get_by_national_id(self, the_national_id):
        print("GET By National_id :", the_national_id)

