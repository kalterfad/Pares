from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str = ''
    is_active: bool = False
    is_superuser: bool = False

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int = 0
    user: str = ''
    date_created: str = ''
    rating: int = 0
    text: str = ''
    website: str = ''

    class Config:
        orm_mode = True


class ReviewUserLinkBase(BaseModel):
    id: str
    user_id: int
    review_id: int

    class Config:
        orm_mode = True


class ReviewsCount(BaseModel):
    id: int = 0
    reviews_count: int = 0
    place_id: str = 0

    class Config:
        orm_mode = True