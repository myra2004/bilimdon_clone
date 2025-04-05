# from datetime import datetime, date
#
# from pydantic import BaseModel
#
#
# class UserSchema(BaseModel):
#     id: int
#     first_name: str
#     last_name: str
#     username: str
#     birthdate: date
#
# dummy_data = {
#     "id": 1,
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "John",
#     "birthdate": date(1970, 1, 1)
# }
#
# user = UserSchema(**dummy_data)
# user_dict = user.model_dump()
# user_dict['is_user'] = True
# print(user.model_dump())