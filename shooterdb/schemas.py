from ninja import Schema


class PersonSchema(Schema):
    id: int
    fname: str
    sname: str
    date_of_birth: str
    club: str
    
class CompetitionSchema(Schema):
    id: int
    name: str
    date: str

class ResultSchema(Schema):
    id: int
    shooter: int
    competition: int
    discipline: str
    score: float
    rank: int
    series: list