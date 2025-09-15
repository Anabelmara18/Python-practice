from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Dict, Any, List, Literal


class API_auth(BaseModel):

    email : str = Field(..., description="this is email")
    password : str = Field(..., min_length=8, description="this is password")
    confirm_password : str = Field(..., min_length=8, description="this is confirm password")

    @model_validator(mode='after')
    def password_match(cls, values):

        if values.password != values.confirm_password:
            raise ValueError("Password and Confirm Password do not match")
        
        return values
    
pyd_ins = API_auth(**{"email": "anabel@example.com", "password": "password123", "confirm_password": "password456"})
print(pyd_ins)