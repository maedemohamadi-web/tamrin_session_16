from user import *
from datetime import date, timedelta

user1=User("lale","jalili","0452488273",date(2005,4,10),"09191024052","l","aaa","student")
user1.the_phone_number="09122306789"
print(user1)
print(user1.birth_date)
user1.family=5
print(user1.family)
print(user1.the_national_id)
print(user1.role)
user1.role="employee"
print(user1)
#user1.role=0
#print(user1)
user1.role="employee"
user1.role=1
print(user1)