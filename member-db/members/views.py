from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.views.generic import View
from django.shortcuts import redirect

# Create your views here.
def members(request):
    template = loader.get_template('home.html')
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')
    member = Member.objects.get(id=id)
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

class MemberAddView(View):
    def get(self, request):
        template = loader.get_template('add.html')
        member = Member()
        context = {
            'member': member,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        joined_date = request.POST.get('joined_date')

        member = Member()
        member.firstname = firstname
        member.lastname = lastname
        member.phone = int(phone)
        member.joined_date = joined_date
        member.save()

        return redirect('/members')

class MemberEditView(View):
    def get(self, request, id):
        template = loader.get_template('edit.html')
        member = Member.objects.get(id=id)
        context = {
            'member': member,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request, id):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        joined_date = request.POST.get('joined_date')

        member = Member.objects.get(id=id)
        member.firstname = firstname
        member.lastname = lastname
        member.phone = int(phone)
        member.joined_date = joined_date
        member.save()

        return redirect('/members')
