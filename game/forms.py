from django import forms
from game.models import Category

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=['username']