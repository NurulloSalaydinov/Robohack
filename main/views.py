from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *

def home_view(request):
    contest = Contest.objects.all().order_by('-id')[:3]
    event = Event.objects.all().order_by('-id')
    contest_history = HistoryImage.objects.last()
    context = {
        'contests': contest,
        'events': event,
        'history': contest_history,
    }
    return render(request, 'home.html', context)

def contest_detail_view(request, slug):
    # print('bu',type(request.user))
    contest = Contest.objects.get(slug=slug)
    # print(contest)
    time_left = TimeLine.objects.filter(which_contest=contest, left=True)
    time_right = TimeLine.objects.filter(which_contest=contest, left=False)
    icon = UsefullIconContest.objects.filter(which_contest=contest)
    who_event = WhoIsForContest.objects.filter(which_contest=contest)
    what_take = WhatTookContest.objects.filter(which_contest=contest)

    context = {
        'object': contest,
        'time_lefts': time_left,
        'time_rights': time_right,
        'icons': icon,
        'who_events': who_event,
        'what_takes': what_take,
    }
    return render(request, 'detail.html', context)

def event_detail_view(request, slug):
    event = Event.objects.get(slug=slug)
    context = {'object': event}
    return render(request, 'event_detail.html', context)


def contact_add_view(request):
    data = json.loads(request.GET.get('data'))
    name = data['name']
    phone = data['phone']
    message = data['message']
    if name != '' and phone != '' and message != '':
        form = Contact.objects.create(name=name, phone=phone, message=message)
        form.save()
        return JsonResponse({'success': 200})
    else:
        return JsonResponse({'error': 400})

def contest_register_view(request):
    data = json.loads(request.GET.get('data'))
    name = data['name']
    phone = data['phone']
    age = data['age']
    experience = data['experience']
    message = data['message']
    contest_id = data['id']
    if name != '' and phone != '' and message != '' and age != '' and experience != '':
        form = ContestRegister.objects.create(full_name=name, phone=phone, about=message, age=age, experience=experience, which_contest=Contest.objects.get(id=contest_id))
        form.save()
        return JsonResponse({'success': 200})
    else:
        return JsonResponse({'error': 400})
    return JsonResponse({'success': 200})

def contest_question_view(request):
    data = json.loads(request.GET.get('data'))
    name = data['name']
    phone = data['phone']
    age = data['age']
    message = data['message']
    contest_id = data['id']
    if name != '' and phone != '' and message != '' and age != '':
        form = ContestQuestion.objects.create(full_name=name, phone=phone, about=message, age=age, contest=Contest.objects.get(id=contest_id))
        form.save()
        return JsonResponse({'success': 200})
    else:
        return JsonResponse({'error': 400})
    return JsonResponse({'success': 200})


########################################################################
########################################################################


########################################################################
########################################################################

def event_register_view(request):
    data = json.loads(request.GET.get('data'))
    name = data['name']
    phone = data['phone']
    age = data['age']
    experience = data['experience']
    message = data['message']
    contest_id = data['id']
    if name != '' and phone != '' and message != '' and age != '' and experience != '':
        form = EventRegister.objects.create(full_name=name, phone=phone, about=message, age=age, experience=experience, which_event=Event.objects.get(id=contest_id))
        form.save()
        return JsonResponse({'success': 200})
    else:
        return JsonResponse({'error': 400})
    return JsonResponse({'success': 200})

def event_question_view(request):
    data = json.loads(request.GET.get('data'))
    name = data['name']
    phone = data['phone']
    age = data['age']
    message = data['message']
    contest_id = data['id']
    if name != '' and phone != '' and message != '' and age != '':
        form = EventQuestion.objects.create(full_name=name, phone=phone, about=message, age=age, event=Event.objects.get(id=contest_id))
        form.save()
        return JsonResponse({'success': 200})
    else:
        return JsonResponse({'error': 400})
    return JsonResponse({'success': 200})


