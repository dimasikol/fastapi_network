from sqlalchemy.orm import Mapped

from ..app.model_default import BaseModel #MixinDateCreateUpdateModel
from datetime import datetime


class User(BaseModel):
    __tablename__ = 'users'
    login: Mapped[str]
    hashed_password: Mapped[str]
    email: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    second_name: Mapped[str]
    avatar: Mapped[str]
    born: Mapped[datetime]
    city: Mapped[str]
    is_active: Mapped[bool]
    is_staff: Mapped[bool]
    is_visible: Mapped[bool]
    klass: Mapped[int]
    liter_klass: Mapped[str]

    reputation: Mapped[int]
    knowledge: Mapped[int]
    secret_key: Mapped[int]

    #albom_images: Mapped[list[int]]
    #messages: Mapped[list[int]]


class Subscribe(BaseModel):
    __tablename__ = 'subscribe'
    user_to: Mapped[int]
    user_from: Mapped[int]


class Friendship(BaseModel):
    __tablename__ = 'friendship'
    user_to: Mapped[int]
    user_from: Mapped[int]


class FriendshipRequest(BaseModel):
    __tablename__ = 'friendship_request'
    user_to: Mapped[int]
    user_from: Mapped[int]


class Message(BaseModel):
    __tablename__ = 'message'
    message: Mapped[str]
    user_from: Mapped[int]
    user_to: Mapped[int]
    visible: Mapped[bool]


class Albom(BaseModel):
    __tablename__ = 'albom'
    image: Mapped[str]
    user: Mapped[int]

