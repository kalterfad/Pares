from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int
    user: str
    date_created: str
    rating: int
    text: str

    class Config:
        orm_mode = True


class ReviewUserLinkBase(BaseModel):
    id: str
    user_id: int
    review_id: int

    class Config:
        orm_mode = True
