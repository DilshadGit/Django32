from django import forms


from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    # create_date = forms.DateTimeField()


    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dict
    #     print(cleaned_data, ' <<< cleaned data')
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'python':
    #         raise form.ValidationError('This title is taken')
    #     print(title, ' << title')
    #     return title

    # this method will clean all data fields
    def clean(self):
        cleaned_data = self.cleaned_data
        print('All fields', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'python':
            self.add_error('title', 'This title is taken.')
            # raise form.ValidationError('This title is taken')
        if 'python' in content or 'python' in title:
            self.add_error('content', 'Python can not be in the content')
            raise form.ValidationError('The article is already taken')
        return cleaned_data
