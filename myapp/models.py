from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)


    def __str__(self):
        return self.username

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')


    def __str__(self):
        return self.name

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time_seconds = models.IntegerField()
    status = models.BooleanField(default=False)  # False - "Не просмотрено", True - "Просмотрено"

    def __str__(self):
        return f"{self.user.username} - {self.lesson.name}"

