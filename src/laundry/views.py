from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView
from .form import LaundryForms





class HomeView(TemplateView):
    """Rendering the Template and other GET or POST request """


    template = 'home.html'


    def get(self, request):
        form_laundry = LaundryForms()
        context = { "form_laundry" : form_laundry }
        return render(request, self.template, context)

    def post(self, request):
        if request.method == 'POST':
            form_laundry = LaundryForms(request.POST)

            if form_laundry.is_valid():
                form_laundry.save()

                return HttpResponseRedirect('/home/')

        context =  { "form_laundry" : form_laundry }
        return render(request, self.template, context )
