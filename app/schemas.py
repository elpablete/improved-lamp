import pydantic
import datetime as dt
import enum as enum


class NullStringPlaceHolder(str, enum.Enum):
    null = ""


class ParticipatingEmployee(pydantic.BaseModel):
    name: str
    id: int
    signature: NullStringPlaceHolder


class HeightWorkSchemaCreate(pydantic.BaseModel):
    execution_date: dt.datetime
    height_from_floor_in_centimeters: int
    participating_employees: list[ParticipatingEmployee]


class HeightWorkSchema(HeightWorkSchemaCreate):
    id: int
