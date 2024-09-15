# blog/widgets.py
from django import forms

class TagWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        tags = value or []
        tag_string = ', '.join([tag.name for tag in tags])
        return forms.TextInput().render(name, tag_string, attrs)

