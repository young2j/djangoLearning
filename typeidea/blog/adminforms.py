from django import forms
from dal import autocomplete
from .models import Category, Tag, Post

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类'
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签'
    )

    # content = forms.CharField(widget=CKEditorWidget,label='正文',required=True)
    content_ck = forms.CharField(widget=CKEditorUploadingWidget,label='正文',required=False)
    content_md = forms.CharField(widget=forms.Textarea,label='正文',required=False)
    content = forms.CharField(widget=forms.HiddenInput,required=False)

    class Meta:
        model = Post
        fields = ['category', 'tag', 'title', 'desc', 'use_md','content', 'content_ck','content_md','status']

    def __init__(self,instance=None,initial=None,**kwargs):
        initial = initial or {}
        if instance:
            if instance.use_md:
                initial['content_md'] = instance.content
            else:
                initial['content_ck'] = instance.content
        super().__init__(instance=instance,initial=initial,**kwargs)

    def clean(self):
        use_md = self.cleaned_data.get('use_md')
        if use_md:
            content_field_name = 'content_md'
        else:
            content_field_name = 'content_ck'
        content = self.cleaned_data.get(content_field_name)
        if not content:
            self.add_error(content_field_name,'必填项')
            return
        self.cleaned_data['content'] = content
        return super().clean()

    class Media:
        js = ('js/post_editor.js',)