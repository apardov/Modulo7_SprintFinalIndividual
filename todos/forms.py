from django import forms

from accounts.models import RegisterUserModel
from .models import TodosUserModel, LabelTodosModel, PriorityUserModel


class CreateTodoForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=LabelTodosModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    user = forms.ModelChoiceField(
        queryset=RegisterUserModel.objects.all(),
        required=False
    )

    priority = forms.ModelChoiceField(
        queryset=PriorityUserModel.objects.all(),
        required=False
    )

    class Meta:
        model = TodosUserModel
        fields = '__all__'


class ViewTodoForm(forms.ModelForm):
    status = forms.ChoiceField(choices=TodosUserModel.STATUS_CHOICES, required=False)
    labels = forms.ModelMultipleChoiceField(queryset=LabelTodosModel.objects.all(), required=False)
    observations = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = TodosUserModel
        fields = ['status', 'labels', 'observations', 'priority']
