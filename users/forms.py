from django import forms
from django.contrib.auth import password_validation
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


# 18.3 참고, 장고에 있는 UserCreationForm을 사용하면 다양한 기능을 사용할 수 있음. (password validation같은)
# from django.contrib.auth.forms import UserCreationForm
# class SignUpForm(UserCreationForm):
#     username = form.EmailField(label="Email")
# UserCreationForm을 사용하지 않은 이유: username을 email과 동일하게 맞춰주기 위해서.
# password validation기능은 UserCreationForm에 들어가서 관련 method들을 가져와서 적용시키면 됨. (import password_validation) 아래에 새로 적용시킴


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First_name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last_name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password1 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmed Password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        try:
            password_validation.validate_password(password1, self.instance)
            if password == password1:
                return password
            else:
                raise forms.ValidationError("Password confirmation does not match")
        except forms.ValidationError as error:
            self.add_error("password", error)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
