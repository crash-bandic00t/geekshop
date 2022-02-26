from django import forms
from mainapp.models import Category, Products
from authapp.models import User
from django.core.exceptions import ValidationError


class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        desc_widget = {
            'class': 'form-control',
            'rows': 3
        }
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['desc'].widget.attrs.update(desc_widget)
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['category'].empty_label = 'Выберите категорию'


class AddUserForm(forms.ModelForm):

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'groups',
                   'date_joined', 'is_superuser', 'last_login']
        # 'first_name', 'last_name', 'email', 'age', 'city', 'avatar', 'is_staff', 'is_active']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают!")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_staff' and field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check'
