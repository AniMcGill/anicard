from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MembershipCard(models.Model):
    design = models.ImageField(upload_to="cards/")
    year_start = models.DateField()
    year_end = models.DateField()
    open = models.BooleanField(default=True)

    def __unicode__(self):
        return "Membership: {}-{}".format(self.year_start.year, self.year_end.year)

    def year(self):
        return self.year_start.year


class CardRequest(models.Model):
    user = models.ForeignKey(User)
    year = models.ForeignKey(MembershipCard)
    printed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    lost = models.BooleanField(default=False)

    def name(self):
        return self.user.get_full_name()

    def __unicode__(self):
        return "{}: {}".format(self.name(), self.year.year())
