from django import forms

class AuthenticationForm(forms.Form):
    """
    Login form
    """

    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = [ 'email', 'password' ]
