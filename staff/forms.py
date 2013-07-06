from django.forms import ModelForm
from staff.models import detail
class TestForm(ModelForm):
    class Meta:
        model=detail

