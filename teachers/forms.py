from django.forms import ModelForm
from teachers.models import Details
class TestForm(ModelForm):
    class Meta:
        model=Details

