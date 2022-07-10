from django import forms

class FormularioLogin(forms.Form):
    user_name = forms.CharField(label = 'Usuario')
    password = forms.CharField(label = 'Password')

    class Meta:
        fields = ('user_name','user_password',)
        labels = {'user_name':'User', 'user_password':'Password'}