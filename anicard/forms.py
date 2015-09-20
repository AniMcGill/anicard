from django import forms


class CardReqForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="Given Name", widget=forms.TextInput(
        attrs={'required': 'required'}))
    last_name = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'required': 'required'}), label="Family Name")
