from django.forms import ModelForm
from students.models import details
class TestForm(ModelForm):
    class Meta:
        model=details

