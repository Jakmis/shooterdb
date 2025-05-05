from collections import defaultdict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Person, Result, Club

# Create your views here.

def home_view(request):
    persons = Person.objects.order_by('person_id')[:3]
    persons_count = Person.objects.all().count()

    context = {
        'persons': persons,
        'persons_count': persons_count,
    }	

    return render(request, 'index.html', context)

def person_list_view(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

def person_detail_view(request, person_id):
    person = get_object_or_404(Person, person_id=person_id)

    is_shooter = hasattr(person, 'shooter')
    is_trainer = hasattr(person, 'trainer')
    is_referee = hasattr(person, 'referee')

    results_by_discipline = defaultdict(list)
    best_results = {}
    trainer = None
    referee = None
    if is_shooter:
        results = Result.objects.filter(shooter=person.shooter).select_related('discipline', 'competition')
        for result in results:
            disc_name = result.discipline.name
            results_by_discipline[disc_name].append(result)

        for disc, res_list in results_by_discipline.items():
            best_result = max(res_list, key=lambda x: x.score)
            best_results[disc] = best_result

    if is_trainer:
        trainer = person.trainer
    if is_referee:
        referee = person.referee



    context = {
        'person': person,
        'is_shooter': is_shooter,
        'is_trainer': is_trainer,
        'is_referee': is_referee,
        'results_by_discipline': results_by_discipline,
        'best_results': best_results,
        'trainer': trainer,
        'referee': referee,
    }

    return render(request, 'person_detail.html', context)

def club_list_view(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})

def club_detail_view(request, club_id):
    club = get_object_or_404(Club, club_id=club_id)
    return render(request, 'club_detail.html', {'club': club})