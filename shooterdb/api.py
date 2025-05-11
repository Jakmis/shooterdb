from ninja import NinjaAPI
from .models import Person, Competition, Result
from .schemas import PersonSchema, CompetitionSchema, ResultSchema
from typing import List

api = NinjaAPI()


@api.get("/persons/", response=List[PersonSchema])
def list_persons(request):
    persons = Person.objects.select_related('club').all()
    return [
        PersonSchema(
            id=p.id,
            fname=p.fname,
            sname=p.sname,
            date_of_birth=p.date_of_birth.strftime('%Y-%m-%d'),  
            club=str(p.club)
        )
        for p in persons
    ]

@api.get("/competitions/", response=List[CompetitionSchema])
def list_competitions(request):
    competitions = Competition.objects.all()
    return [
        CompetitionSchema(
            id=c.id,
            name=c.name,
            date=str(c.date)
        )
        for c in competitions
    ]

@api.get("/results/", response=List[ResultSchema])
def list_results(request):
    results = Result.objects.select_related('shooter', 'competition', 'discipline').all()
    return [
        ResultSchema(
            id=result.id,
            shooter=result.shooter.id,  
            competition=result.competition.id, 
            discipline=str(result.discipline), 
            score=result.score,
            rank=result.rank,
            series=result.series
        )
        for result in results
    ]