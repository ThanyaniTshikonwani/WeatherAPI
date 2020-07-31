from django import forms


class Post(forms.Form):
    post = forms.CharField(label="post", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter city'}))
