from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Employee
from .tasks import clear_paid_salary_task


# Register your models here.
@admin.action(description="Clear paid salary")
def clear_paid_salary(modeladmin, request, queryset):
    if len(queryset) > 20:
        clear_paid_salary_task.delay(queryset)
    else:
        queryset.update(paid_salary=0)


@admin.register(Employee)
class EmployeeTreeAdmin(MPTTModelAdmin):
    mptt_level_indent = 0
    list_display = (
        'full_name',
        'position',
        'parent',
        'salary',
        'paid_salary',
    )
    list_filter = (
        'level',
        'position',
    )
    actions = [clear_paid_salary]
