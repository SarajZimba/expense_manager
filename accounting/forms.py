from django import forms
from .models import Expense, ExpenseCategory

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date', 'expense_category', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select date', 'type': 'date'}),
            'expense_category': forms.Select(attrs={'class': 'form-select', "data-control":"select2"}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter notes', 'rows': 3}),
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['expense_category'] = forms.ModelChoiceField(queryset=ExpenseCategory.objects.filter(is_deleted=False))
    
    #     self.fields["expense_category"].widget.attrs = {
    #         "class":"form-select",
    #         "data-control": "select2",
    #         "data-placeholder": "Select Category",
    #     }
