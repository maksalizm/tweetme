from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must loggin in "])
            return self.form_invalid(form)
