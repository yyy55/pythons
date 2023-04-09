from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    # 优先到当前目录寻找（需要提前到settings.py配置）【不配置就是无效】
    # 然后根据app注册顺序寻找
    # 去app目录下的templates目录寻找user_list.html（根据app注册顺序，逐一去templates目录找）
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


def tpl(request):
    name = '就是卡德罗夫'
    role = ['管理员', '用户']
    user = {'name': '123', 'sex': '男'}
    return render(request, 'tpl.html', {'n1': name, 'n2': role, 'n3': user})


def news(req):
    # http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news
    import requests
    print(11)
    res = requests.post('http://124.70.218.186:8088/api/colleges/selectByList', json={})
    print(res)
    data_list = res.json()
    print(data_list)
    return render(req, 'news.html', {'data_list': data_list})

def something(request):

    print(request.method)
    print(request.GET)
    print(request.POST)
    return HttpResponse(request.method)
