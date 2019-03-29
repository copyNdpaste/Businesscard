from django import forms

class HTMLForm(forms.Form):
    text = forms.CharField(
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'text 입력',
                'style': 'color:red',
            }
        )    
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '패스워드 입력'}
        )
    )
    hidden = forms.CharField(
        widget=forms.HiddenInput()
    )
    textarea = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 50, 'rows': 20}
        )
    )
    radio = forms.CharField(
        widget=forms.RadioSelect(
            choices=(('a', 'A'), ('b', 'B'))
        )
    )
    number = forms.IntegerField(label='정수')
    check = forms.BooleanField()
    choice = forms.ChoiceField(choices=(('code', '코드'), ('A', '에이')))
    date = forms.DateField(
        input_formats='%Y-%m-%d',
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )