from django import forms
from .models import Students, Teachers, News, StudentsAchievement, InformationSchool


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class AchievementForm(forms.ModelForm):
    class Meta:
        model = StudentsAchievement
        fields = '__all__'


class InformationSchoolForm(forms.ModelForm):
    class Meta:
        model = InformationSchool
        fields = '__all__'
