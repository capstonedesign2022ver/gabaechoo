from django.shortcuts import render, redirect
from . import main
import random
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import user_info
from .models import Test
from .models import Rating

array1 = np.zeros((20, 20))
username =''
test = Test()
rating = Rating()
def home(request):
    return render(request, 'home.html')


def info1(request):
    return render(request, 'info1.html')


@csrf_exempt
def info2(request):

    return render(request, 'info2.html')


def info3(request):

    return render(request, 'info3.html')

'''
def info4(request):
    chk_fur1 = request.POST.getlist('chk_fur1[]')
    kname = []
    kname1 = request.POST.getlist('Kname1[]')
    if (len(kname1) == 1):
        kname11 = list(map(int, kname1[0].split(',')))
        kname.append(kname11)

    kname2 = request.POST.getlist('Kname2[]')
    if (len(kname2) == 1):
        kname22 = list(map(int, kname2[0].split(',')))
        kname.append(kname22)
    kname3 = request.POST.getlist('Kname3[]')
    if (len(kname3) == 1):
        kname33 = list(map(int, kname3[0].split(',')))
        kname.append(kname33)

    kname4 = request.POST.getlist('Kname4[]')
    if (len(kname4) == 1):
        kname44 = list(map(int, kname4[0].split(',')))
        kname.append(kname44)

    kname5 = request.POST.getlist('Kname5[]')
    if (len(kname5) == 1):
        kname55 = list(map(int, kname5[0].split(',')))
        kname.append(kname55)

    kname6 = request.POST.getlist('Kname6[]')
    if (len(kname6) == 1):
        kname66 = list(map(int, kname6[0].split(',')))
        kname.append(kname66)

    kname7 = request.POST.getlist('Kname7[]')
    if (len(kname7) == 1):
        kname77 = list(map(int, kname7[0].split(',')))
        kname.append(kname77)
        print(kname77[0])
        print(type(kname77[0]))
    array1 = main.fixgenerate(chk_fur1, kname)
    print("fix")
    print(array1)
    return render(request, 'info4.html', {'array1': array1})
'''

def recommend(request):
    '''msize = request.POST.get('size')
    chk_fur2 = request.POST.getlist('chk_fur2[]')
    array1 = main.addgenerate(chk_fur2)
    back = Image.new('RGB', (400, 400), '#AAAAAA')
    back.save("002.png")
    for i in range(1, 10):
        main.show_image1(array1, i, "002.png")
    image = Image.open("002.png")
    image.save('추천.png')
    image.show()'''
    chk_fur1 = request.POST.getlist('chk_fur1[]')
    kname = []; kname11=[]; kname22=[]; kname33=[]; kname44=[]; kname55=[]; kname66=[]; kname77=[];
    kname1 = request.POST.getlist('Kname1[]')
    if (len(kname1) == 1):
        kname11 = list(map(int, kname1[0].split(',')))
        if(kname11[0] != 0):
            kname.append(kname11)
    kname2 = request.POST.getlist('Kname2[]')
    if (len(kname2) == 1):
        kname22 = list(map(int, kname2[0].split(',')))
        if (kname22[0] != 0):
            kname.append(kname22)
    kname3 = request.POST.getlist('Kname3[]')
    if (len(kname3) == 1):
        kname33 = list(map(int, kname3[0].split(',')))
        if (kname33[0] != 0):
            kname.append(kname33)
    kname4 = request.POST.getlist('Kname4[]')
    if (len(kname4) == 1):
        kname44 = list(map(int, kname4[0].split(',')))
        if (kname44[0] != 0):
            kname.append(kname44)
    kname5 = request.POST.getlist('Kname5[]')
    if (len(kname5) == 1):
        kname55 = list(map(int, kname5[0].split(',')))
        if (kname55[0] != 0):
            kname.append(kname55)
    kname6 = request.POST.getlist('Kname6[]')
    if (len(kname6) == 1):
        kname66 = list(map(int, kname6[0].split(',')))
        if (kname66[0] != 0):
            kname.append(kname66)
    kname7 = request.POST.getlist('Kname7[]')
    if (len(kname7) == 1):
        kname77 = list(map(int, kname7[0].split(',')))
        if (kname77[0] != 0):
            kname.append(kname77)
    array1 = main.fixgenerate(chk_fur1, kname)

    return render(request, 'recommend.html', {'array1': array1})

def home2(request):
    input = request.POST['chk_info']
    if input == '1':
        rating1 = 1
    elif input == '2':
        rating1 =2
    elif input == '3':
        rating1 =3
    elif input == '4':
        rating1 =4
    elif input == '5':
        rating1 =5
    test.rating = rating1
    test.save()
    return render(request, 'home.html')


def image(request):
    return render

# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                            first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            auth.login(request, user)
            userInfo = user_info()
            userInfo.gender = request.POST['gender']
            userInfo.user = request.user
            userInfo.job = request.POST['job']
            userInfo.year = request.POST['year']
            userInfo.month = request.POST['month']
            userInfo.day = request.POST['day']
            #userID = auth.authenticate(request, username='username', password='password')
            #userinfo = user_info.objects.all
            #userinfo = user_info(user_id=User.id, gender=request.POST['gender'], job=request.POST['job'])
            userInfo.save()
            # 로그인 한다
            auth.login(request, user)
            {'username': username}
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        {'username': username}
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            rating.user_id = username
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')


# 로그 아웃
def logout(request):
    auth.logout(request)
    return redirect('/')
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    #if request.method == 'POST':
    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    #else:
        #return render(request, 'login.html')

# Create your views here.
