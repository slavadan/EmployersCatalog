from CatalogProject.celery import app
from .models import Employee


@app.task
def clear_paid_salary_task(queryset):
    queryset.update(paid_salary=0)


@app.task
def pay_salary():
    employers = Employee.objects.all()

    for employee in employers:
        employee.update(
            paid_salary=employee.salary + employee.paid_salary
        )
