from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal


class addrress(BaseModel):
    
    street: str = Field(..., description="This is street")
    city: str = Field(..., description="This is city")
    state: str = Field(..., description="This is state")
    country: str = Field(..., description="This is country")
    zip_code: str = Field(..., description="This is zip code")

class personal_info(BaseModel):

    name: str = Field(...,min_length=3,max_length=20, description="this is name")
    age: int | None = Field(..., gt=0, description="this is age")
    email : str = Field(..., description="this is email")
    address: addrress = Field(..., description="this is address")

pyud_ins = personal_info(**{
    "name": "Anabel", 
    "age": 25, 
    "email": "anabel@example.com", 
    "address": addrress(**{
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "country": "USA",
        "zip_code": "62701"})
    })

print(pyud_ins)