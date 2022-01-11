from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Costs(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Пользователь', blank = True, null = True)
    title = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    data = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    place_where_spent = models.CharField(max_length=150)
    comments = models.TextField(blank=True)

    def get_update_url(self):
        return reverse('update_costs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-data']

class Inkome(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    title = models.CharField(max_length=150, blank=True)
    data = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['-data']
