import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from .room_scraper import IFoodie
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.db.models import Count

# from .showsheet import Showgoosheet


# Create your views here.
def home(request):
    return render(request, "home.html")


def rwd(request):
    if request.method == "POST":
        obj = Testfarm()
        
        form = EditTestform(request.POST, instance=obj)
        
        print(form.is_valid())
        if form.is_valid():
            print(form)
            form.save()
            print("--------------New Text Add ----------------")
            return redirect("/rwd")

    return render(
        request,
        "rwd.html",
        {
            "rwd_acrive": "active",
        },
    )


def test(request):
    return render(
        request,
        "test.html",
        {
            "test_active": "active",
        },
    )


# 文章列表


def text(request):
    # tag_num = Textfarm.objects.
    text_list = Textfarm.objects.all().order_by("-time_create")
    for_grp = Textfarm.objects.values('tag').order_by('-tag').annotate(count=Count('tag'))
    list_num = Textfarm.objects.count()
    print("here is ")
    print(text_list[0].tag)  # web
    return render(
        request,
        "text/Text.html",
        {
            "text_active": "active",
            "text_list": text_list,
            "list_num": list_num,
            "grp_list":for_grp,

        },
    )


# 新增文章
def text_add(request):

    if request.method == "POST":
        obj = Textfarm()
        obj.creator = request.user
        print(request.POST)
        form = EditTextForm(request.POST, instance=obj)
        print("--------------New Text Add ----------------")
        if form.is_valid():
            print(form)
            form.save()
            return redirect("/text")

    form = EditTextForm(None)
    context = {"text_active": "active", "form": form}

    return render(request, "text/Text_add.html", context)


# 文章首頁


def text_detail(request, pk):

    post = Textfarm.objects.get(pk=pk)

    return render(
        request,
        "text/Text_detail.html",
        {
            "post": post,
            "text_active": "active",
        },
    )


# 刪除文章


def text_delete(request, pk):

    obj = Textfarm.objects.get(pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect("/text")

    context = {
        "text_active": "active",
        "obj": obj,
    }
    return render(request, "text/Text_delete.html", context)


def text_edit(request, pk):

    obj = Textfarm.objects.get(pk=pk)

    form = EditTextForm(request.POST or None, instance=obj)
    context = {
        "form": form,
    }
    if form.is_valid():
        obj.time_edit = datetime.datetime.now()
        obj.creator = str(request.user)
        form.save()

        print("--------------You successfully updated the post------")

        url = "/text/" + str(pk)
        return redirect(url)
    else:
        context = {
            "form": form,
            "text_active": "active",
            "title": obj.title,
            "creator": obj.creator,
            "time_create": obj.time_edit,
            "error": "The form was not updated successfully. Please enter in a title and content",
        }
        return render(request, "text/Text_edit.html", context)


"""
    if request.method == "POST":
        form = EditTextForm(request.POST, instance=post)

        print('------------------------')
        print(form.title)
        print('------------------------')

        print('------------------------')
        print(request.POST)
        print('------------------------')
        if form.is_valid():
            form.save()
            url = '/'
            return redirect(url)  #重新導向到登入畫面
        else:
            print('fail')

    else:#GET
        form = EditTextForm(initial={'title': post.title,
                                     'time_create': post.time_create,
                                     'body': post.body})
        context = {
            'form': form
        }

        return render(request, 'Text_edit.html',context)
"""


# 註冊
def sign_up(request):

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")  # 重新導向到登入畫面
    context = {"form": form}
    return render(request, "auth/register.html", context)


# 登入


def sign_in(request):
    form = LoginForm()
    context = {"form": form}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            return redirect("/")  # 重新導向到首頁
    context = {"form": form}
    return render(request, "auth/login.html", context)


# 登出


def log_out(request):
    auth.logout(request)
    return redirect("/login")  # 重新導向到登入畫面


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect("/")
    else:
        return render(request, "auth/login.html", locals())


def diary(request):
    diary_list = DiaryWrite1.objects.all()
    return render(
        request,
        "diary.html",
        {
            "Diary_active": "active",
            "post_list": diary_list,
        },
    )


def find_food(request):
    # obj = Showgoosheet().select()
    print(request)
    if request.method == "POST":
        return redirect("query")
    return render(
        request,
        "findfood.html",
        {
            "title": "首頁",
            "Home_active": "active",
        },
    )


def comment(request):
    food = IFoodie(request)
    return redirect(food.get_comment(request.GET["rest_name"]))


# 找食物
@csrf_exempt
def query(request):

    food = IFoodie(request.GET["area"], request.GET["catagory"])
    food.scrape()

    return render(
        request,
        "foodlist.html",
        {
            "Home_active": "active",
            "res_list": food.content,
        },
    )


def error_404(request, exception):
    # 40481
    response = render(request, "error.html")
    response.status_code = 404
    return response


def error_500(request):
    # 4041231
    response = render(request, "error.html")
    response.status_code = 500
    return response
