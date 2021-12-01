from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import ModelFile


# モデルからフォームを作成
class FormAnimal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # htmlの表示を変更可能にします
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control-file'

    class Meta:
        model = ModelFile  # 画像ファイル送信用 フォームモデル
        fields = ('image',)  # form 項目には画像を指定 , が無いとerror


# ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # htmlの表示を変更可能にします
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


# サインアップフォーム
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # htmlの表示を変更可能にします
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
