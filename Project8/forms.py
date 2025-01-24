
from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    Fullname=forms.CharField(
        widget=forms.TextInput(attrs={"class":'form-control',"maxlength":50}),

    )
    Email=forms.EmailField(
        widget=forms.EmailInput(attrs={"class": 'form-control'})
    )
    Message=forms.CharField(
        widget=forms.Textarea(attrs={"class": 'form-control'})
    )


class Loginform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"نام کاربری خود را وارد کنید"})
    )

    password=forms.CharField(
       widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"رمز عبور را وارد کنید"})
    )

User = get_user_model()
class Registerform(forms.Form):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری خود را وارد کنید"})
    )

    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور را وارد کنید"})
    )

    password2 = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "مجددا رمز عبور را وارد کنید"})
    )

    Email=forms.EmailField(
        label="email",
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"ایمیل خود را وارد کنید"})

    )

    def clean_username(self):
        userName = self.cleaned_data.get('username')
        query=User.objects.filter(username=userName)
        if query.exists():
            raise forms.ValidationError("نام کاربری تکراری است")
        return userName

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("رمز عبور مطابقت ندارد")
        return data


