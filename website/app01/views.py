from django.shortcuts import render, HttpResponse
from app01 import models
from django import forms


# Create your views here.

class UserInfoModelForm(forms.ModelForm):
    is_rmb = forms.CharField(widget=forms.CheckboxInput())

    class Meta:
        model = models.UserInfo
        fields = '__all__'

        labels = {
            'username': '用户名',
            'email': '邮箱',
        }

        help_texts = {
            'username': 'please input your username',
        }

        widgets = {
            'username': forms.Textarea(attrs={'class': 'c1'})
        }

        error_messages = {
            '__all__': {},
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误..',
            }
        }

        field_classes = {

        }

    def clean_username(self):
        old = self.cleaned_data['username']
        return old


class UserInfoForm(forms.Form):
    username = forms.CharField(max_length=32)
    email = forms.EmailField()
    user_type = forms.ChoiceField(
        choices=models.UserType.objects.values_list('id', 'caption')
    )

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id', 'caption')


def index(request):
    if request.method == 'GET':
        obj = UserInfoModelForm
        return render(request, 'index.html', {'obj': obj})
    elif request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():
            instance = obj.save(False)
            instance.save()
            obj.save_m2m()
        return render(request, 'index.html', {'obj': obj})


def user_list(request):
    li = models.UserInfo.objects.all().select_related('user_type')
    return render(request, 'user_list.html', {'li': li})


def user_edit(request, nid):
    if request.method == 'GET':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})
    elif request.method == 'POST':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})

