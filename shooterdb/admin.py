from django.contrib import admin
from .models import Result, Club, Person, Shooter, Specialization, Trainer, Referee, Gun, Discipline, Category, Competition
from .forms import ResultForm

# Person
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'fname', 'sname', 'date_of_birth', 'club')
    search_fields = ('fname', 'sname', 'person_id')

# Shooter
@admin.register(Shooter)
class ShooterAdmin(admin.ModelAdmin):
    list_display = ('person',)
    search_fields = ('person__fname', 'person__sname')

# Trainer
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('person', 'license_number')
    search_fields = ('person__fname', 'person__sname', 'license_number')

# Referee
@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ('person', 'license_number')
    search_fields = ('person__jmeno', 'person__prijmeni', 'license_number')

# Klub
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_id', 'name')
    search_fields = ('club_id', 'name')

# Gun
@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    list_display = ('gun_type', 'brand', 'model', 'caliber', 'owner')
    search_fields = ('brand', 'model', 'owner__person__fname', 'owner__person__sname')

# Discipline
@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'distance')

# Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Specialization
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('code',)

# Competition
@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    filter_horizontal = ('disciplines', 'referees', 'categories')

# Result with validation
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    form = ResultForm
    list_display = ('shooter', 'competition', 'discipline', 'category', 'score', 'rank')
    search_fields = ('shooter__person__fname', 'shooter__person__sname')
    list_filter = ('competition', 'discipline', 'category')
