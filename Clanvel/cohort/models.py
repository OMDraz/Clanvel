from django.utils import timezone 
from django.db import models 
from django.urls import reverse 
from clanvel import models as core_models 
from cal import Calendar 


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True 
    
    def __str__(self):
        return self.name 

class CohortName(AbstractItem):
    """ CohortActivities """ 

    class Meta:
        verbose_name = "Cohort Name"

class CohortLocations(AbstractItem):
    """ Cohort Locations """
    pass 

    class Meta:
        verbose_name_plural = "Cohort Locations"

class CohortRules(AbstractItem):
    """ Cohort Based Rules """
    class Meta:
        verbose_name = "Cohort Rules"

class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """ 
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="cohort_photos")
    cohort = models.ForeignKey("Cohort", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption 


class Cohort(core_models.TimeStampedModel):
    """ Cohort Definition """
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )
    name = models.CharField(max_length=140)
    description = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField() 
    guests = models.IntegerField(help_text="How many will be participating?")
    size = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    cohort_guide = models.ForeignKey(
        "accounts.User", related_name="cohort", on_delete=models.CASCADE 
    )
    cohortName = models.ManyToManyField(CohortName, related_name="cohort", blank=True)
    cohortLocations = models.ManyToManyField(CohortLocations, related_name="cohort", blank=True)
    cohortRules = models.ManyToManyField(CohortRules, related_name="cohort", blank=True)
    
    username = None
    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cohort:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all() 
        all_ratings = 0 
        if len(all_reviews) > 0:
            for review in all_reviews: 
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0 

    def first_photo(self):
        try:
            photo, =self.photos.all()[:1]
            return photo.file.url 
        except ValueError:
            return None 
    
    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos 

    def get_calendars(self):
        now = timezone.now()
        this_year = now.year 
        this_month = now.month 
        next_month = this_month + 1 
        if this_month == 12:
            next_month = 1 
        this_month_cal = Calendar(this_year, this_month)
        next_month_cal = Calendar(this_year, next_month) 
        return [this_month_cal, next_month_cal]

