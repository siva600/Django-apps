from django import forms

from products.models import Product


class RawProductForm(forms.Form):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs=
                            {
                                "placeholder": "Your Title"
                            }))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs=
                                  {

                                      "class": "new-class-name two",
                                      "placeholder": "Your Description",
                                      "id": "my-id-for-textarea",
                                      "rows": 10,
                                      "cols": 20,
                                  }))
    price = forms.DecimalField(initial='000.00')
