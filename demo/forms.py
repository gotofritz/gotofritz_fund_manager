from django import forms


class UploadFileForm(forms.Form):
    """The form for uploading the funds list.

    Given more time I would have used crispy_forms with tailwind, and
    something like

    def __init__(self):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper() self.helper.layout = Layout( ...
    """

    file = forms.FileField(
        widget=forms.FileInput(attrs={"class": "csv-upload"}),
        label="Upload a new list of funds",
    )
