from django.db import models
from django.contrib.auth.models import User

maxCharLength = 128


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=maxCharLength)
    middle_name = models.CharField(max_length=maxCharLength, blank=True)
    surname = models.CharField(max_length=maxCharLength)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non Binary'),
        ('PNTD', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, blank=True)
    picture = models.ImageField(upload_to='profilePics', blank=True)

    # rating = models.FloatField()


    def __str__(self):
        return self.user.username


class Destination(models.Model):
    # must be related to the map API used somehow.
    locationName = models.TextField(unique=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.locationName

class TravelNote(models.Model):
    # owner = models.ForeignKey(User)
    content = models.TextField(blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, blank=True)
    travelPics = models.ImageField(upload_to="travelPics", blank=True)


class TravelHistory(models.Model):
    # owner = models.ForeignKey(User)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    travelPics = models.ImageField(upload_to="travelPics", blank=True)
    travelNotes = models.ForeignKey(TravelNote, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name_plural = 'TravelHistories'
    
class TravelWishlist(models.Model):
    # owner = models.ForeignKey(User)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    travelNotes = models.ForeignKey(TravelNote, on_delete=models.CASCADE)

class UpcomingTravel(models.Model):
    # owner = models.ForeignKey(UserProfile, default='', unique=False, on_delete=models.CASCADE)
    owner = models.CharField(null=False, max_length=maxCharLength, blank=False, default="testing3")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    budgetStart = models.DecimalField(max_digits=6, decimal_places=2)
    budgetEnd = models.DecimalField(max_digits=6, decimal_places=2)
    # travelNotes = models.ForeignKey(TravelNote, on_delete=models.CASCADE, blank=True)


class ForumPost(models.Model):
    # author = models.ForeignKey(User)
    title = models.CharField(max_length=maxCharLength)
    date = models.DateField() # default needs to be current date
    content = models.TextField()

class PostReply(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    # author = models.ForeignKey(User)
    title = models.CharField(max_length=maxCharLength)
    date = models.DateField() # default needs to be current date
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'PostReplies'

