from django import forms

from .models import ModelFile


# モデルからフォームを作成
class FormAnimal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control-file'

    class Meta:
        model = ModelFile  # 画像ファイル送信用 フォームモデル
        fields = ('image',)  # form 項目には画像を指定 , が無いとerror
