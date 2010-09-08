from django.forms import ModelForm
from models import *

class ContributionForm(ModelForm):
    class Meta:
        model = Contribution