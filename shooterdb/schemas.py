from ninja import Schema

class PersonSchema(Schema):
    person_id: int
    fname: str
    sname: str

# class VysledekSchema(Schema):
#     id: int
#     body: int
#     poradi: int