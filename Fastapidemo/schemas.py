from pydantic import BaseModel
class Productschema(BaseModel):
    
    id: int
    name: str
    desc: str
    price: float