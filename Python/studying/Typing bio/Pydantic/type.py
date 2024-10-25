from pydantic import BaseModel, StrictStr, StrictInt, StrictBool, StrictBool 

class UserModel(BaseModel):
    username: StrictStr
    

user = UserModel(username="Alice")