from django import forms


class SignUpForm(forms.Form):
    month = [(0, 'Month'), (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'),
             (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]
    gender = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    confirm_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Confirm email',
                                                                   'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    month = forms.ChoiceField(choices=month, widget=forms.Select(attrs={'class':'form-control'}))
    day = forms.IntegerField(min_value=1, max_value=31, widget=forms.NumberInput(attrs={'placeholder': 'Day',
                                                                                      'class': 'form-control'}))
    year = forms.IntegerField(min_value=1950, max_value=2017, widget=forms.NumberInput(attrs={'placeholder': 'Year',
                                                                                            'class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender)
