
# continuing the above example...
from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    

    
egor = User(name="Egor")
print(egor.id, egor.name)