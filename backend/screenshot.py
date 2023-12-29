from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
import base64
import load_agent_database
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from openai import OpenAI
import requests
from difflib import SequenceMatcher
import json

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def scroll():

  driver = webdriver.Chrome()

  # Navigate to the website
  driver.get('https://atlanta.craigslist.org/')

  # Obtain the initial window dimensions
  window_size = driver.get_window_size()
  width = window_size['width']
  height = window_size['height']

  # Double the height of the window
  driver.set_window_size(width, height)

  if not os.path.exists('screenshots'):
      os.makedirs('screenshots')

  # Get the initial scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")
  max_height = driver.execute_script("return document.body.scrollHeight;")
  print("max heihgt"+ str(max_height))
  heihgt=-500
  counter = 1
  driver.save_screenshot(f'screenshots/scroll_{0}.png')

  while True:
      # Scroll by the height of the window
      driver.set_window_size(width, height)

      driver.execute_script("window.scrollBy(0, window.innerHeight*1);")

      # Wait to load page
      time.sleep(2)  # Sleep for 2 seconds or you can use WebDriverWait for a better approach

      # Take a screenshot
      counter += 1
      driver.save_screenshot(f'screenshots/scroll_{counter}.png')

      # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      current_scroll_position = driver.execute_script("return window.pageYOffset;")
      if(current_scroll_position==last_height):
          break
      last_height=current_scroll_position
      print("new Hieght"+ str(new_height))
      print("current index"+ str(current_scroll_position))


      if new_height-700<=current_scroll_position: 
          break

  # Close the WebDriver
  driver.quit()

def click(url,buttontext):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    link = driver.find_element(By.LINK_TEXT, buttontext)
    link.click()
    time.sleep(2)
    driver.quit()

# Handles Browser Click interaction. Buttontext is the text of the button the user wants to click ,driver is the selenium object, flag is wheter or not an clickable element ist provided from previous interactions.
    
def browser_click(buttontext,driver,flag, els_list): 
  try: 
    print("Linked text")
    link = driver.find_element(By.LINK_TEXT, buttontext)
    link.click()
  except: 
    try: 
        print("Name text")
        link = driver.find_element(By.NAME,buttontext)
        link.click()
    except: 
     if flag: 
        closest_element = []
        closest_distance = 0.0
        clickable_elements = driver.find_elements(By.XPATH,"//a | //button | //input[@type='button'] | //input[@type='submit']")
        elements_with_pointer_cursor = driver.find_elements(By.CSS_SELECTOR,"*:hover")
        clickable_elements_with_role = driver.find_elements(By.XPATH,"//*[@role='button']")
        all_clickable_elements = elements_with_pointer_cursor +clickable_elements_with_role+clickable_elements

        print("The length of the clickable elements "+ str(len(all_clickable_elements)))
        for element in all_clickable_elements:
                try:
                    parent = element.find_element(By.XPATH,'..') # Gets the immediate parent element
                    distance = float(similar(parent.text, buttontext))
                    print(distance)
                    if distance == closest_distance:
                        closest_element.append(element)
                    elif distance > closest_distance: 
                        closest_element=[]
                        closest_element.append(element)
                        closest_distance=distance
                except: 
                 continue
           
        print("Closest element length is"+ str(len(closest_element)))
        for ele in closest_element: 
         try:
            html_content = ele.get_attribute('outerHTML')
            print("The element,"+ str(html_content) )
            ele.click()
            print("super succesful")
            break
         except: 
           print("Nope failed")
     else: 
        print("conrrect way")
        closest_element = []
        closest_distance = 0.0
        for element in els_list: 
             try:
                    parent = element.find_element(By.XPATH,'..') # Gets the immediate parent element
                    print(parent.text)
                    distance = float(similar(parent.text, buttontext))
                    print(distance)
                    if distance == closest_distance:
                        closest_element.append(element)
                    elif distance > closest_distance: 
                        closest_element=[]
                        closest_element.append(element)
                        closest_distance=distance
             except: 
                 continue
        for ele in closest_element: 
         try:
            html_content = ele.get_attribute('outerHTML')
            # print("The element,"+ str(html_content) )
            ele.click()
            print("super succesful")
            break
         except: 
           print("Nope failed")
           
    print("Done")
  time.sleep(1)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  

def textbox(url):
#  driver = webdriver.Firefox()
 driver = uc.Chrome()


  # Navigate to the website
 driver.get(url)
 time.sleep(5)
 driver.implicitly_wait(45)
 driver.save_screenshot(f'screenshots/scroll_{1}.png')
 try:
    textbox=driver.find_element(By.TAG_NAME,"input")
    #  textbox=driver.find_elements(By.NAME,"q")
    #  print(len(textbox))
    #  textbox=textbox[1]
    type=textbox.get_attribute('aria-label')
    print(type)
    textboxstr= str(textbox.get_attribute('innerHTML'))
    if textboxstr.__contains__("search"):
        print("true")
        print(textboxstr)
    else:
        print("false")
    #  for input_element in inputs:
    #     print(input_element.get_attribute('type'))  
    

    element_class = textbox.get_attribute('class')
    element_id = textbox.get_attribute('id')
    print(f"Class: {element_class}, ID: {element_id}")
    print(textboxstr)
    textbox.send_keys("6 Hawk Court")
    textbox.send_keys(Keys.ENTER)
 except:
    try:
        textbox=driver.find_element(By.TAG_NAME,"textarea")
        #  textbox=driver.find_elements(By.NAME,"q")
        #  print(len(textbox))
        #  textbox=textbox[1]
        type=textbox.get_attribute('aria-label')
        print(type)
        textboxstr= str(textbox.get_attribute('innerHTML'))
        if textboxstr.__contains__("search"):
            print("true")
            print(textboxstr)
        else:
            print("false")
        #  for input_element in inputs:
        #     print(input_element.get_attribute('type'))  
        

        element_class = textbox.get_attribute('class')
        element_id = textbox.get_attribute('id')
        print(f"Class: {element_class}, ID: {element_id}")
        print(textboxstr)
        textbox.send_keys("6 Hawk Court")
        textbox.send_keys(Keys.ENTER)
    except: 
       print("failed")
def find_search_field(driver):
    # List of potential selectors for search fields and textareas
    selectors = [
        "input[type='search']",  # HTML5 search input
        "input[name*='search']", # Input where 'name' contains 'search'
        "input[id*='search']",   # Input where 'id' contains 'search'
        "input[class*='search']",# Input where 'class' contains 'search'
        "textarea[name*='search']", # Textarea where 'name' contains 'search'
        "textarea[id*='search']",   # Textarea where 'id' contains 'search'
        "textarea[class*='search']",# Textarea where 'class' contains 'search'
        "//input[@type='text']",     # XPath, generic text input
        "//textarea",               # XPath, any textarea
        # Add more selectors as needed
    ]
    returnlist=[]
    for selector in selectors:
        try:
            # Try CSS selector
            if selector.startswith(("//", "/")):
                element = driver.find_elements(By.XPATH, selector)
                returnlist.append(element)
            else:
                element = driver.find_elements(By.CSS_SELECTOR, selector)
                returnlist.append(element)
            # if element:
            #     return element
        except :
            continue
    flattened_list = [item for sublist in returnlist for item in sublist]
    return flattened_list
def browser_search(driver,searchterm):
 driver.implicitly_wait(25)
 try:
    textbox=driver.find_element(By.TAG_NAME,"input")
    type=textbox.get_attribute('aria-label')
    print(type)
    element_class = textbox.get_attribute('class')
    element_id = textbox.get_attribute('id')
    print(f"Class: {element_class}, ID: {element_id}")
    textbox.send_keys(searchterm)
    textbox.send_keys(Keys.ENTER)
 except:
    try:
        textbox=driver.find_element(By.TAG_NAME,"textarea")
        type=textbox.get_attribute('aria-label')
        print(type)
        element_class = textbox.get_attribute('class')
        element_id = textbox.get_attribute('id')
        print(f"Class: {element_class}, ID: {element_id}")
        textbox.send_keys(searchterm)
        textbox.send_keys(Keys.ENTER)
    except: 
        try:
            elements=find_search_field(driver)
            for ele in elements:
              try:
                type=textbox.get_attribute('aria-label')
                print(type)
                element_class = textbox.get_attribute('class')
                element_id = textbox.get_attribute('id')
                print(f"Class: {element_class}, ID: {element_id}")
                textbox.send_keys(searchterm)
                textbox.send_keys(Keys.ENTER)
              except:
                print("skip")
        except: 
            print("failed")
    

 time.sleep(1)

def decode_vision_json(dict1): 
    # dict= json.loads(dict)
    print(dict1)
    message=dict1['choices'][0]['message']
    content=message['content']
    print(type(content))
    print(content)
    try:
       if not (content.__contains__('{')):
          content='{'+content+'}'
       content= json.loads(content)
       for key in content:
        if key=='button':
            return (True,content[key])
        else: 
            return (False, content[key])
    except:
        json_string = '\n'.join(content.split('\n')[1:-1])
        data = json.loads(json_string)
        for key in data:
            if key=='button':
                return (True,data[key])
            else: 
                return (False, data[key])
    

    # content=json.loads(content)
   


# click("https://atlanta.craigslist.org/","electronics")
            

def get_all_clickable_elements(driver):
    clickable_elements = driver.find_elements(By.XPATH,"//a | //button | //input[@type='button'] | //input[@type='submit']")
    elements_with_pointer_cursor = driver.find_elements(By.CSS_SELECTOR,"*:hover")
    clickable_elements_with_role = driver.find_elements(By.XPATH,"//*[@role='button']")
    all_clickable_elements = elements_with_pointer_cursor +clickable_elements_with_role+clickable_elements
    totalstr=""
    ellist=[]
    for element in all_clickable_elements:
            try:
                parent = element.find_element(By.XPATH,'..') # Gets the immediate parent element
                parent_text= str(parent.text)
                if len(parent_text)>1 and len(parent_text)<90 and not totalstr.__contains__(parent_text): 
                   parent_text=parent_text.replace("\n", "")
                   totalstr+=parent_text +"\n"
                   ellist.append(element)
                # else: 
                # #    print("Search not included: "+ parent_text)
                   

            except: 
               continue
    return (totalstr,ellist)


def navigate(agent,url,website_context,key):
  options = uc.ChromeOptions()

# Add arguments to options
  options.add_argument("enable-automation")
  options.add_argument("--headless")
  options.add_argument("--window-size=1920,1080")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-extensions")
  options.add_argument("--dns-prefetch-disable")
  options.add_argument("--disable-gpu")
  options.set_capability("pageLoadStrategy", "normal")
  driver = uc.Chrome(options=options)

  # Navigate to the website
  driver.get(url)
  context=""
  # Obtain the initial window dimensions
  window_size = driver.get_window_size()
  width = window_size['width']
  height = window_size['height']

  # Double the height of the window
  driver.set_window_size(width, height)

#   if not os.path.exists('screenshots'):
#       os.makedirs('screenshots')

  # Get the initial scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")
  max_height = driver.execute_script("return document.body.scrollHeight;")
  print("max height"+ str(max_height))
  counter = 1      
  while counter< 7: 
    time.sleep(2)
    (clickable,elslist)=get_all_clickable_elements(driver)
    screenshot= driver.get_screenshot_as_base64()
    print("Clickable elements driver "+ clickable)
    tup= decode_vision_json(agent.vision_test(key,screenshot,website_context,context,clickable))
    print("Length of element list"+ str(len(elslist)))
    if tup[0]==True: 
       browser_click(tup[1],driver,False,elslist)
       context+=" Button Click: "+ str(tup[1])
    else: 
       browser_search(driver,tup[1])
       context+= "Searched up"+ str(tup[1])

    counter+=1
    print("Context "+ context)
  driver.quit()

  
key="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"
# # img0=encode_image('.\screenshots\scroll_0.png')
# # img1= encode_image('.\screenshots\scroll_1.png')


marlene=load_agent_database.LoadAgent('rbp94@cornell.edu','marlene')
# # dict=(marlene.vision_test(key,img0,"This is a website that allows you to buy things that you want to purchase locally"))
# # # test={'id': 'chatcmpl-8a7S3XYO1iz0BX8QesZuK3WVtIHJI', 'object': 'chat.completion', 'created': 1703619143, 'model': 'gpt-4-1106-vision-preview', 'usage': {'prompt_tokens': 1956, 'completion_tokens': 16, 'total_tokens': 1972}, 'choices': [{'message': {'role': 'assistant', 'content': '```json\n{\n  "button": "real estate for sale"\n}\n```'}, 'finish_reason': 'stop', 'index': 0}]}
# # print(decode_vision_json(dict))

navigate(marlene,"https://airbnb.com","This is a website that allows you to get short term rental properties","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")


# driver=uc.Chrome()
# driver.get("https://airbnb.com")
# time.sleep(12)
# els=(get_all_clickable_elements(driver))
# print(len(els))
# for el in els: 
#    print(el)
# print(els)