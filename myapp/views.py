from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.


def input(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        alignment = request.POST.get('alignment', '')
        img = request.POST.get('img', '')
        ac = request.POST.get('ac', '')
        hp = request.POST.get('hp', '')
        speed = request.POST.get('speed', '')
        str = request.POST.get('str', '')
        dex = request.POST.get('dex', '')
        con = request.POST.get('con', '')
        int = request.POST.get('int', '')
        wis = request.POST.get('wis', '')
        cha = request.POST.get('cha', '')
        skills = request.POST.get('skills', '')
        senses = request.POST.get('senses', '')
        languages = request.POST.get('languages', '')
        cr = request.POST.get('cr', '')
        passives = request.POST.get('passives', '')
        actions = request.POST.get('actions', '')
        legendary = request.POST.get('legendary', '')

        profile = Profile(name=name, desc=desc, alignment=alignment, img=img, ac=ac, hp=hp,
                          speed=speed, str=str, dex=dex, con=con, int=int, wis=wis, cha=cha, skills=skills,
                          senses=senses, languages=languages, cr=cr, passives=passives, actions=actions, legendary=legendary)
        profile.save()
    return render(request, 'pdf/input.html')


def monsterblock(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/monsterblock.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "monsterblock.pdf"

    return response


def monsterlist(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/monsterlist.html', {'profiles': profiles})



