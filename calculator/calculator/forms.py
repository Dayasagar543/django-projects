from django import forms

class calculator(forms.Form):
    input1 = forms.IntegerField(label='First Value')
    input2 = forms.IntegerField(label='Second Value')
    operation = forms.ChoiceField(choices=[('add', 'Add'), ('subtract', 'Subtract'), ('multiply', 'Multiply'), ('divide', 'Divide')], label='Operation')
   
    