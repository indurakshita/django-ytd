from django import forms


class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter video url'}), label=False)