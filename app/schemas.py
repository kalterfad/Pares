from pydantic import BaseModel
from typing import List, Union


class UserBase(BaseModel):
    id: int
    username: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int = 0
    user: str = ''
    date_created: str = ''
    rating: int = 0
    text: str = ''

    class Config:
        orm_mode = True


class ReviewUserLinkBase(BaseModel):
    id: str
    user_id: int
    review_id: int

    class Config:
        orm_mode = True


class ReviewsCount(BaseModel):
    id: Union[int, None]
    reviews_count: int
    place_id: str

    class Config:
        orm_mode = True