from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(unique=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Evaluation(Base):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='evaluations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    score = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5),
                    MinValueValidator(0)])

    class Meta:
        unique_together = ('course', 'email')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.score} from {self.course}'
