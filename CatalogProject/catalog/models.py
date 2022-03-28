from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Employee(MPTTModel):
    full_name: models.CharField = models.CharField(max_length=50)
    position: models.CharField = models.CharField(max_length=50)
    employment_date: models.DateField = models.DateField()
    salary: models.PositiveIntegerField = models.PositiveIntegerField()
    paid_salary: models.PositiveIntegerField = models.PositiveIntegerField()
    parent: TreeForeignKey = TreeForeignKey(
        'self',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='subordinate',
        verbose_name='chief',
    )
    user: models.OneToOneField = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.full_name
