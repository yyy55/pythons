# https://www.bilibili.com/video/BV1NL41157ph?p=1&vd_source=713bcfe12546c14d7ca38c2cda87861a

settings.py文件里边57行删除
删除templates目录
python manage.py startapp app


到【INSTALLED_APPS】里边注册

# 安装依赖的
pip install requests
pip install mysqlclient

#对数据库创建或者修改的
python manage.py makemigrations
python manage.py migrate