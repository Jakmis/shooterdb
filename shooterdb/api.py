from ninja import NinjaAPI
from .models import Person
from .schemas import PersonSchema

api = NinjaAPI()


@api.get("/persons/", response=list[PersonSchema])
def get_persons(request):
    return Person.objects.all()