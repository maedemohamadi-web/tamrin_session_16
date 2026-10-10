from datetime import date
from persian_tools import national_id,phone_number

#اسامی رو طوری نوشتم که با کلمات کلیدی اشتباه گرفته نشه
class User:
    def __init__(self, name, family, the_national_id, birth_date, the_phone_number, user_name, password, role,locked=False):
        self.name = name
        self.family = family
        self.the_national_id = the_national_id
        self.birth_date = birth_date
        self.the_phone_number = the_phone_number
        self.user_name = user_name
        self.password = password
        self.role=role
        self.locked = locked

    #name getter,setter,property
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name=name
        else:
            print("Invalid name")

    name=property(get_name, set_name)

    # family getter,setter,property
    def get_family(self):
        return self.__family

    def set_family(self, family):
        if isinstance(family, str):
            self.__family = family
        else:
            print("Invalid family")

    family = property(get_family, set_family)

    # the_national_id getter,setter,property
    def get_national_id(self):
        return self.__the_national_id

    def set_national_id(self, the_national_id):
        if isinstance(the_national_id, str) and national_id.validate(the_national_id):
            self.__the_national_id= the_national_id
        else:
            print("Invalid national id")

    the_national_id = property(get_national_id, set_national_id)

    # birth_date getter,setter,property
    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        if not isinstance(birth_date, date):
            raise ValueError("Birth Date Invalid !!!")

       # if 20<birth_date<40:
            self.role="employee"
        #else:
            #print("The employee can be between 20 and 40 years old!")
        self.__birth_date = birth_date
        age=(date.today()-birth_date).days//365
        if 20<age<40:
            self.role="employee"


    birth_date = property(get_birth_date, set_birth_date)

    # the_phone_number getter,setter,property
    def get_phone_number(self):
        return self.__the_phone_number

    def set_phone_number(self, the_phone_number):
        if isinstance(the_phone_number, str) and phone_number.validate(the_phone_number):
            self.__the_phone_number = the_phone_number

    the_phone_number = property(get_phone_number, set_phone_number)

    #user_name getter,setter,property
    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        if isinstance(user_name, str):
            self.__user_name = user_name

    user_name = property(get_user_name, set_user_name)

    #password getter,setter,property
    def get_password(self):
        return self.__password

    def set_password(self, password):
        if isinstance(password,str):
           self.__password = password

    password = property(get_password, set_password)

    #role getter,setter,property
    def get_role(self):
        return self.__role

    def set_role(self, role):
        if isinstance(role, str) :
            self.__role = role
        else:
            print("Invalid role")

    role = property(get_role, set_role)

    def __repr__(self):
        return f"User({self.__dict__})"
