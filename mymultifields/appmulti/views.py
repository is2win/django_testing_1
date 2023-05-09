from django.shortcuts import render
from django.views.generic import ListView
from .models import Forward, Option
from django.views.generic.edit import UpdateView
from django.forms import modelform_factory, inlineformset_factory


class ForwardListView(ListView):
    model = Forward
    template_name = 'appmulti/forward_list.html'
    context_object_name = 'forwards'


class ForwardUpdateView(UpdateView):
    model = Forward
    fields = ['forward_class']
    template_name = 'appmulti/edit_forward.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OptionFormSet = inlineformset_factory(Forward, Option, fields=('name', 'description', 'type_of_field'), extra=1)
        if self.request.POST:
            data['option_formset'] = OptionFormSet(self.request.POST, instance=self.object)
        else:
            data['option_formset'] = OptionFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        option_formset = context['option_formset']
        if option_formset.is_valid():
            self.object = form.save()
            option_formset.instance = self.object
            option_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
