# pip install selenium
# 谷歌插件下载
# https://registry.npmmirror.com/binary.html?path=chromedriver/

# 导入驱动
from selenium import webdriver
# 导入驱动服务
from selenium.webdriver.chrome.service import Service
# 导入by包进行元素定位
from selenium.webdriver.common.by import By
# 导入时间相关服务
import time,datetime
# 导入web驱动等服务
from selenium.webdriver.support.ui import WebDriverWait
# 导入条件预设组件
from selenium.webdriver.support import expected_conditions as EC
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 驱动服务指定路径，路径指向chromedriver.exe
    s=Service("./chromedriver_mac_arm64/chromedriver")
    # 谷歌浏览器选项
    options=webdriver.ChromeOptions()
    # 添加debugger模式启动谷歌浏览器
    options.add_experimental_option("debuggerAddress","127.0.0.1:6001")
    # 初始化谷歌浏览器服务
    # driver=webdriver.Chrome(options=options,service=s)
    driver=webdriver.Chrome(service=s)
    # 打开网址
    

