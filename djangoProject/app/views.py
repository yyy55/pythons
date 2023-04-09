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

def something(request):

    print(request.method)
    print(request.GET)
    print(request.POST)
    return HttpResponse(request.method)

from app.models import *
def orm(request):
    # 测试orm操作表中的数据
    # # 添加数据
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='IT部')
    # Department.objects.create(title='打杂部')

    # UserInfo.objects.create(name='admin',password='123',age=19)
    # UserInfo.objects.create(name='user',password='123',age=20)

    # 删除
    # # 删除id为3的
    # UserInfo.objects.filter(id=1).delete()
    # # 删除全部
    # UserInfo.objects.all().delete()

    #查询数据
    # # 查询所有数据，数组
    # list = UserInfo.objects.all()
    # print(list)
    # for li in list:
    #     print(li.id,li.name,li.password,li.age)
    # # 得到id为3的数据，类似根据条件查询，是一个数组
    # list = UserInfo.objects.filter(id=3)
    # # 查询id为3的数据，只需要1条数据
    # user = UserInfo.objects.filter(id=3).first()
    # # 根据条件修改数据
    # UserInfo.objects.filter(id=4).update(name='user')
    return HttpResponse(list)
