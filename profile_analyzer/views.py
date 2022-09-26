from django.shortcuts import render
from .api_wrapper import github as github
from profile_analyzer.models import Candidate
from django.urls import reverse
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect


def index(request):

    return render(request, 'profile_analyzer/homepage.html')


def search_page(request):

    search_value = request.GET.get('q')
    page = request.GET.get('page')
    if page == None:
        page = 1
    else:
        page = int(page)
    platform = request.GET.get('btnradio')
    result = github.make_api_search_request(search_value, page)
    for i in result['items']:
        print(i['login'])
        user = github.get_user(i['login'])
        try:
            i['bio'] = user['bio']
            i['location'] = user['location']
        except:
            print('An exception occurred while getting bio and location')

    return render(request, 'profile_analyzer/list.html', {'searchresult': result, 'search_q': search_value, 'page': page})


def adduser(request, username):
    user = github.get_user(username)
    c = Candidate(username=user['login'],
                  bio=user['bio'],
                  location=user['location'],
                  avatar_url=user['avatar_url'],
                  html_url=user['html_url']
                  )
    c.save()
    return HttpResponseRedirect(reverse('candidate_list'))


def del_candidate(request, username):
    options = {'message': ''}
    try:
        c = Candidate.objects.filter(username=username)
        c.delete()
        print("The user is deleted")

    except Candidate.DoesNotExist:
        print("User doesnot exist")
        return HttpResponseRedirect(reverse('candidate_list'))

    except Exception as e:
        return HttpResponseRedirect(reverse('candidate_list'))

    return HttpResponseRedirect(reverse('candidate_list'))


class CandidateListView(ListView):

    model = Candidate
    paginate_by = 5
    title = "List of candidates"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
