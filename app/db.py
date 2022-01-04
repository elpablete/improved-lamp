from .schemas import HeightWorkSchema, HeightWorkSchemaCreate

DB = []


def create_height_works_in_db(height_work: HeightWorkSchemaCreate) -> HeightWorkSchema:
    new = height_work.dict()
    new["id"] = len(DB) + 1
    DB.append(new)
    in_db = HeightWorkSchema.parse_obj(new)
    return in_db


def get_height_works_from_db(id: int) -> HeightWorkSchema:
    found = [hw for hw in DB if hw["id"] == id]
    if len(found) == 0:
        raise ValueError(f"HeightWork with id {id} not found")
    elif len(found) > 1:
        raise ValueError(f"Multiple HeightWorks with id {id} found")
    in_db = HeightWorkSchema.parse_obj(found[0])
    return in_db
