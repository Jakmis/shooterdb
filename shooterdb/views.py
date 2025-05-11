from collections import defaultdict
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Result, Club, Competition, Gun, Shooter, Discipline, Trainer
from .forms import PersonForm, ClubForm, CompetitionForm, ResultForm, GunForm, TrainerForm

# Create your views here.

def home_view(request):
    competitions = Competition.objects.order_by('-date')[:5]
    context = {
        'competitions': competitions,
        'shooter_count': Shooter.objects.count(),
        'trainer_count': Trainer.objects.count(),
        'competition_count': Competition.objects.count(),
        'discipline_count': Discipline.objects.count(),
    }
    return render(request, 'index.html', context)

def person_list_view(request):
    persons = Person.objects.all()
    query = request.GET.get('q')
    if query:
        persons = persons.filter(
            Q(fname__icontains=query) |
            Q(sname__icontains=query) |
            Q(person_id__icontains=query)
        )

    return render(request, 'person_list.html', {'persons': persons, 'query': query})

def person_detail_view(request, person_id):
    person = get_object_or_404(Person, person_id=person_id)

    is_shooter = hasattr(person, 'shooter')
    is_trainer = hasattr(person, 'trainer')
    is_referee = hasattr(person, 'referee')

    trainer = None
    referee = None
    if is_shooter:
        results = Result.objects.filter(shooter=person.shooter)

    if is_trainer:
        trainer = person.trainer
    if is_referee:
        referee = person.referee

    context = {
        'person': person,
        'is_shooter': is_shooter,
        'is_trainer': is_trainer,
        'is_referee': is_referee,
        'results': results,
        'trainer': trainer,
        'referee': referee,
    }

    return render(request, 'person_detail.html', context)

def person_create_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    
    return render(request, 'person_create.html', {'form': form})

def club_list_view(request):
    clubs = Club.objects.all()
    query = request.GET.get('q')
    if query:
        clubs = clubs.filter(
            Q(name__icontains=query) |
            Q(club_id__icontains=query)
        )
    return render(request, 'club_list.html', {'clubs': clubs, 'query': query})

def club_detail_view(request, club_id):
    club = get_object_or_404(Club, club_id=club_id)
    shooters = Person.objects.filter(club=club).select_related('shooter')
    shooters_count = shooters.count()
    context = {
        'club': club,
        'shooters': shooters,
        'shooters_count': shooters_count,
    }
    return render(request, 'club_detail.html', context)

def club_create_view(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('club_list')
    else:
        form = ClubForm()
    
    return render(request, 'club_create.html', {'form': form})

def competition_list_view(request):
    competitions = Competition.objects.all()
    query = request.GET.get('q')
    if query:
        competitions = competitions.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(date__icontains=query) |
            Q(disciplines__name__icontains=query)
        )
    return render(request, 'competition_list.html', {'competitions': competitions, 'query': query})

def competition_detail_view(request, pk):
    competition = get_object_or_404(Competition, pk=pk)
    results = Result.objects.filter(competition=competition)
    shooters = defaultdict(list)
    for result in results:
        shooters[result.shooter].append(result)

    context = {
        'competition': competition,
        'results': results,
        'shooters': shooters,
    }
    return render(request, 'competition_detail.html', context)

def competition_create_view(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competition_list')
    else:
        form = CompetitionForm()
    
    return render(request, 'competition_create.html', {'form': form})

def result_create_view(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = ResultForm()
    return render(request, 'result_create.html', {'form': form})

def gun_create_view(request):
    if request.method == 'POST':
        form = GunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gun_list')
    else:
        form = GunForm()
    return render(request, 'gun_create.html', {'form': form})

def gun_list_view(request):
    guns = Gun.objects.all()
    query = request.GET.get('q')
    if query:
        guns = guns.filter(
            Q(brand__icontains=query) |
            Q(model__icontains=query) 
        )
    return render(request, 'gun_list.html', {'guns': guns, 'query': query})

def trainer_create_view(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = TrainerForm()
    return render(request, 'trainer_create.html', {'form': form})