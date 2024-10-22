from .model_default import MixinDateCreateUpdateModel, BaseModel
from sqlalchemy import TEXT

class SubCategory(MixinDateCreateUpdateModel):
    title: [str]
    image: [str]
    text: [TEXT]

class Category(MixinDateCreateUpdateModel):
    title: [str]
    image: [str]
    text: [TEXT]

class Tags(BaseModel):
    title: [str]

class News(MixinDateCreateUpdateModel):
    title: [str]
    image: [str]
    text: [TEXT]


