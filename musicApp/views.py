from django.shortcuts import render,redirect
from . import models 
import requests


# Create your views here.
def homepage(request):
    url = "https://saavn.dev/api/albums?language=hindi"
    response = requests.request("GET", url)
    print(response.json())
    return render(request, 'index.html', context={"data": response.json()})


def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pswd']
        user = models.UserProfile.objects.filter(email=email,password=password)
        # print(user.all().values()[0]['id'])
        if len(user) == 1:
            # request.session['user'] = user.all().values()[0]['id'] 
            print("Successfully login")
            return redirect('/')
        else :
            print("error")
    return render(request, 'login.html')


def mymusicpage(request):
    return render(request, 'mymusic.html')


def playlistpage(request, id):

    return render(request, 'Playlistdetails.html')


def signuppage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        contact = request.POST['contact']
        email = request.POST['email']
        s1 = models.UserProfile(username = username,password= password,contact=contact,email=email)
        s1.save()
        return redirect('/login')

    return render(request, 'signup.html')


def showlist(request, id):
    url = f'https://saavn.dev/playlists?id={id}'
    response = requests.request("GET", url)
    print(response.json()['data']['songs'][0]['id'])
    return render(request, 'showlist.html', context={'playlist': response.json()['data'],'link':response.json()['data']['songs'][0]['id']})
    


def showalbum(request, id):
    url = f'https://saavn.dev/api/albums?id={id}'
    response = requests.request("GET", url)
    print(response.json())
    return render(request, 'showalbum.html', context={'albums': response.json()['data']})


def likepage(request):
    return render(request, 'like.html')


def songplay(request, string_id):
    
    url = f'https://saavn.dev/api/songs/{string_id}'
    response = requests.request("GET", url)
    print(response.json()['data'][0])
    return render(request, 'songplay.html', context={'songs': response.json()['data'][0]})


def searchpage(request):
    # print(request.session['user'])
    # del request.session['user'] 
    # if request.session['user']:
    #     pass
    # else:
    #     redirect('/login')
    url = "https://saavn.dev/api/search"
    if request.method == 'POST':
        query = request.POST['search']
        querystring = {"query":query}
        response = requests.get(url, params=querystring)
        # print(response.json())
        return render(request, 'like.html', context={"data": response.json()})
    else:
        querystring = {"query":"new"}
        response = requests.get(url, params=querystring)
        # print(response.json())
        return render(request, 'like.html', context={"data": response.json()})
