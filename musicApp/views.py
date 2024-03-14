from django.shortcuts import render
import requests


# Create your views here.
def homepage(request):
    url = "https://saavn.dev/api/albums?language=hindi"
    response = requests.request("GET", url)
    print(response.json())
    return render(request, 'index.html', context={"data": response.json()})


def loginpage(request):
    return render(request, 'login.html')


def mymusicpage(request):
    return render(request, 'mymusic.html')


def playlistpage(request, id):

    return render(request, 'Playlistdetails.html')


def signuppage(request):
    return render(request, 'signup.html')


def showlist(request, id):
    url = f'https://saavn.dev/playlists?id={id}'
    response = requests.request("GET", url)
    print(response.json()['data']['songs'][0]['id'])
    return render(request, 'showlist.html', context={'playlist': response.json()['data'],'link':response.json()['data']['songs'][0]['id']})
    


def showalbum(request, id):
    url = f'https://saavn.dev/albums?id={id}'
    response = requests.request("GET", url)
    # print(response.json())
    return render(request, 'showalbum.html', context={'albums': response.json()['data']})


def likepage(request):
    return render(request, 'like.html')


def songplay(request, string_id):
    
    url = f'https://saavn.dev/api/songs/{string_id}'
    response = requests.request("GET", url)
    # print(response.json()['data'][0])
    return render(request, 'songplay.html', context={'songs': response.json()['data'][0]})


def searchpage(request):
    print(request.session)
    if request.session['isloggedIn']:
        request.session['isloggedIn']
        url = "https://saavn.dev/api/search"
        if request.method == 'POST':
            query = request.POST['search']
            querystring = {"query":query}
            response = requests.get(url, params=querystring)

            print(response.json())
            return render(request, 'like.html', context={"data": response.json()})
        else:
            querystring = {"query":"new"}
            response = requests.get(url, params=querystring)
            print(response.json())
            return render(request, 'like.html', context={"data": response.json()})
    else:
        return render('/login')
