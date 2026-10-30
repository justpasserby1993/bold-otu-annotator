from selenium import webdriver # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait #等待模块
from selenium.webdriver.support import expected_conditions as EC #异常处理
import time  #时间模块，计时
import random #随机模块，滚动用反反爬
import os  # 本地文件目录需要用

#配置
fasta_path = r"C:\Office\WD\Python\split_1.fasta"    #fasta文件目录
output_dir = r"C:\Office\WD\Python\bold_results"  #下载目录

if not os.path.exists(output_dir): #确保指定下载目录
    os.makedirs(output_dir)

#浏览器设置
chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--ignore-certificate-errors') #忽略证书错误
chrome_options.add_argument('--ignore-ssl-errors')  #忽略SSL错误
chrome_options.add_argument('--disable-blink-features=AutomationControlled') #反反爬机制
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 新增反检测参数
chrome_options.add_argument("--start-maximized") #最大化
# 配置下载参数
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": output_dir,  # 下载目录
    "download.prompt_for_download": False,     # 禁用下载提示
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options) # 声明浏览器对象

driver.get('https://id.boldsystems.org/')
print("已打开网站")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("已滚动到底部")
time.sleep(2)  # 确保滚动完成

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))#等待文本粘贴区显示

with open(fasta_path, "r") as f:  #打开文件并读取
    sequence = f.read()

textarea = driver.find_element(By.TAG_NAME, "textarea")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", textarea)
print("成功滚动到当前位置")
textarea.send_keys(sequence)  #粘贴序列
time.sleep(30)
print("已成功粘贴序列")
identify_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )

print("已找到提交按钮")
identify_button.click()
print("已点击提交按钮")
time.sleep(5)
driver.execute_script("window.scrollTo(0, %d)" % random.randint(200, 500)) #随机滚动反反扒机制
time.sleep(1.5)
print("已成功滚动")
time.sleep(30)
download_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Download CSV']]"))
)
print("已找到下载按钮")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", download_button)
print("成功滚动到当前位置")
time.sleep(1)
download_button.click()
print("已触发下载")
time.sleep(10)
print("已成功下载，位置在初始设置的默认下载目录")
driver.close() #关闭浏览器