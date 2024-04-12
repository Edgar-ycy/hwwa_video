from my_edge import AutoEdge
from time import sleep
from selenium.webdriver.common.by import By     # 匹配元素方式
from selenium.webdriver.common.keys import Keys

all_useful_handles = []
driver = AutoEdge()

# 登录
web0 = driver.open_new_window(new_url="http://www.ccsazx.net/#/login")
username = web0.find_element(By.ID, "form_item_username")
password = web0.find_element(By.ID, "form_item_password")

# 输入账号密码并登录
sleep(1)
username.send_keys("13399379495")
password.send_keys("Ycy12569800$",Keys.ENTER)
sleep(2)
# 打开我的课程
web1 = driver.open_new_window(new_url="https://www.ccsazx.net/#/my-course/index")

sleep(5)#加载时间必须长一点，不然只能加载第一页
courses_pagination = web1.find_elements(by=By.XPATH,value=r"//ul/li/a") # 课程页
print(courses_pagination)

pages = len(courses_pagination)# 课程页数
source_handle = driver.get_window_handle()
# 遍历每一页
for this_page in range(pages):
    # 点击页数,
    courses_pagination = web1.find_elements(by=By.XPATH,value=r"//ul/li/a") # 课程页
    if this_page != 0:
            courses_pagination[this_page].click()
    # 获取所有课程
    courses = web1.find_elements(By.XPATH,r"//div[@class='ant-spin-container']/div/div/div/div/div[3]/div/button")
    course_len = len(courses)
    courses_pagination = web1.find_elements(by=By.XPATH,value=r"//ul/li/a") # 课程页
    # 进入每一门课
    for i in range(course_len):
        web_new = driver.open_new_window(new_url="https://www.ccsazx.net/#/my-course/index")
        sleep(3)# 这个必须3秒以上
        
        # 点击页数,
        courses_pagination = web_new.find_elements(by=By.XPATH,value=r"//ul/li/a") # 课程页 
        if this_page != 0:
            courses_pagination[this_page].click()
        # 获取所有课程
        courses = web_new.find_elements(By.XPATH,r"//div[@class='ant-spin-container']/div/div/div/div/div[3]/div/button")
        course_len = len(courses)
        # 进入第几课 
        sleep(1)
        courses[i].click()
        sleep(1)
        # 继续学习
        xvexi = web_new.find_element(By.XPATH,r"/html/body/div/section/section/section/div[2]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/button").click()
        sleep(1)
        
        kuozhan = web_new.find_element(By.XPATH,r"//span[contains(@class, 'ant-tree-switcher') and contains(@class, 'ant-tree-switcher_close')]").click()
        sleep(1)
        per_video = web_new.find_elements(By.XPATH,r"//span[text()='视频']")
        this_url1 = web_new.current_url
        
        # 获取当前页的handle，每一门课的handle
        this_handle1 = driver.get_window_handle()
        
        video = web_new.find_element(By.XPATH,r"/html/body/div/div/div[1]/div[2]/div/div[1]/video")
        sleep(2)
        web_new.execute_script("arguments[0].play();", video) # 打开视频
        web_new.execute_script("arguments[0].playbackRate = 5;", video) # 视频倍速
        sleep(1)
        
        #打开每一个视频
        for video_count in range(1,len(per_video)):
            web_new2 = driver.open_new_window(new_url=this_url1)
            sleep(3)
            # 打开扩展里面的视频
            kuozhan = web_new.find_element(By.XPATH,r"//span[contains(@class, 'ant-tree-switcher') and contains(@class, 'ant-tree-switcher_close')]").click()
            sleep(2)
            per_video = web_new2.find_elements(By.XPATH,r"//span[text()='视频']")
            
            per_video[video_count].click()
            sleep(3)
            video = web_new2.find_element(By.XPATH,r"//*[@id='dPlayerVideoMain']")
            sleep(2)
            web_new2.execute_script("arguments[0].play();", video) # 打开视频
            # input("视频已打开，打开倍速中")
            web_new2.execute_script("arguments[0].playbackRate = 5;", video) # 视频倍速
            # 回到此课程页面
            driver.switch_to_window(this_handle1)
        sleep(2)    
        driver.switch_to_window(source_handle)
        sleep(3)
# driver.keep()
sleep(15*60)
driver.close_all()