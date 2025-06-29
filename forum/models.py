from django.db import models

class AnonymousPost(models.Model):
    MOOD_CHOICES = [
        ('happy', 'HAPPY'),
        ('sad', 'SAD'),
        ('angry', 'ANGRY'),
        ('anxious', 'ANXIOUS'),
        ('neutral','NEUTRAL'),
    ]
    message = models.TextField(max_length=1000)
    mood = models.CharField(max_length=10, choices= MOOD_CHOICES, default= 'neutral')
    created_at = models.DateTimeField(auto_now_add= True)
    likes = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.mood} - {self.message[:50]}"


