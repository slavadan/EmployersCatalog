from CatalogProject.celery import app
from .models import Employee


@app.task
def clear_paid_salary_task(id_list):
    for id in id_list:
        employee = Employee.objects.get(id=id)
        employee.paid_salary = 0
        employee.save()


@app.task
def pay_salary():
    employers = Employee.objects.all()

    for employee in employers:
        employee.paid_salary += employee.salary
        employee.save()
