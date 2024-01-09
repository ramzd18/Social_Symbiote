from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
import base64
from backend import load_agent_database
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from openai import OpenAI
import requests
from difflib import SequenceMatcher
import json
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException,  NoSuchElementException

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuzzywuzzy import fuzz
import itertools
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate



from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

class CustomChrome(uc.Chrome):
    def __del__(self):
        try:
            self.quit()
        except Exception as e:
            print(f"Error in __del__: {e}")




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
                    # parent = element.find_element(By.XPATH,'..') # Gets the immediate parent element
                    # print(parent.text)
                    distance = float(similar(element.text, buttontext))
                    print(distance)
                    if distance == closest_distance:
                        closest_element.append(element)
                    elif distance > closest_distance: 
                        closest_element=[]
                        closest_element.append(element)
                        closest_distance=distance
                    elif element.text.contains(buttontext): 
                        closest_element.append(element)
             except: 
                 continue
        for ele in closest_element: 
         try:
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
            return (True,content[key],content['feedback'])
        else: 
            return (False, content[key],content['feedback'])
    except:
        json_string = '\n'.join(content.split('\n')[1:-1])
        data = json.loads(json_string)
        for key in data:
            if key=='button':
                return (True,data[key],data['feedback'])
            else: 
                return (False, data[key],data['feedback'])
    

    # content=json.loads(content)
   


def is_clickable(element):
    try:
        return element.is_displayed() and element.is_enabled()
    except StaleElementReferenceException:
        return False
def is_element_visible_in_viewpoint(driver, element) -> bool:
   elements_in_viewport = driver.execute_script("""
var elementsInViewPort = [];
var allElements = document.getElementsByTagName('*');

for (var i = 0, max = allElements.length; i < max; i++) {
    var elem = allElements[i];
    var rect = elem.getBoundingClientRect();
    
    if (rect.top >= 0 && rect.left >= 0 && 
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && 
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)) {
        elementsInViewPort.push(elem);
    }
}

return elementsInViewPort;
""")
   return elements_in_viewport


def is_element_clickable(element,driver):
    try:
        # Check if the element is displayed and enabled
        if not (element.is_displayed() and element.is_enabled()):
            return False
        location = element.location
        size = element.size
        x = location['x'] + size['width']/2
        y = location['y'] + size['height']/2
        top_element = driver.execute_script("return document.elementFromPoint(arguments[0], arguments[1]);", x, y)

        if element == top_element:
                return True
        else:
                False 
      

        return True
    except :
        # Element is no longer attached to the DOM
        return False    
    
def split_list(input_list, size):
    return [input_list[i:i + size] for i in range(0, len(input_list), size)]



def get_element_texts(elements):
    return [element.text for element in elements]

def get_texts_of_elements(driver, elements):
    # Use JavaScript to get texts of all elements in one go
    script = """
    return arguments[0].map(function(el) { 
        return el.textContent.trim(); 
    });
    """
    return driver.execute_script(script, elements)



def filter_elements_by_text(driver, elements):
    # Get all texts in one go
    texts = get_texts_of_elements(driver, elements)
    
    # Filter elements based on text length
    return [el for el, text in zip(elements, texts) if 0 < len(text) <= 90]


def compare_texts(text1, text2, similarity_threshold):
    if fuzz.ratio(text1, text2) > similarity_threshold:
        return True
    return False

def remove_similar_strings(elements, similarity_threshold=80):
    element_texts = get_element_texts(elements)
    to_remove = set()

    # Create a thread pool for parallel processing
    with ThreadPoolExecutor() as executor:
        future_to_pair = {executor.submit(compare_texts, text1, text2, similarity_threshold): (i, j) 
                          for i, text1 in enumerate(element_texts)
                          for j, text2 in enumerate(element_texts) if i < j}

        for future in concurrent.futures.as_completed(future_to_pair):
            if future.result():
                i, j = future_to_pair[future]
                shorter_index = i if len(element_texts[i]) < len(element_texts[j]) else j
                to_remove.add(shorter_index)

    results = [element for i, element in enumerate(elements) if i not in to_remove]
    return results

def get_all_clickable_elements(driver):
    wait = WebDriverWait(driver, 5)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

    # elements = driver.find_elements(By.XPATH, "//*")
    elements=is_element_visible_in_viewpoint(driver,"")
    split_size= len(elements)//8
    split_elements= split_list(elements,split_size)

    print("COMPLETE ELEMENTS LENGTH: "+ str(len(elements)))
    clickable_elements=[]
    with ThreadPoolExecutor(max_workers=8) as executor:
      for sublist in split_elements:
            # Execute is_clickable for each element in the sublist
            results = executor.map(lambda el: is_element_clickable(el, driver), sublist)
            clickable_elements.extend([el for el, is_click in zip(sublist, results) if is_click])
    print("DONE COMPILING ALL THIS INFORMATION"+ str(len(clickable_elements)))
    # filtered_els = [element for element in clickable_elements if element.text and (len(element.text.strip())>1 and len(element.text.strip()) <= 90)]
    filtered_els=filter_elements_by_text(driver,clickable_elements)
    print("DONE FILTERING"+ str(len(filtered_els)))
    updated_els_list= remove_similar_strings(filtered_els)
    text_list=get_texts_of_elements(driver,updated_els_list)
    print("UPDATING")
    return updated_els_list


def findtext():
    driver = webdriver.Chrome()
    driver.get("https://airbnb.com")
    # It's better to use explicit waits instead of time.sleep
    time.sleep(10)  # Consider replacing with WebDriverWait for better efficiency

    els = get_all_clickable_elements(driver)
  
    for textval in els:
        print("Example Text: " + textval.text)




def detect_popup(driver):
    overlay_selectors = [
       '[role="dialog"]',
    '[aria-modal="true"]',
    'div[style*="display: block"]',
    'div[style*="position: fixed"]'
]

    for selector in overlay_selectors:
        overlays = driver.find_elements(By.CSS_SELECTOR,selector)
        print("LENGTH OF OVERLAYS"+ str(len(overlays)))
        if overlays and any(overlay.is_displayed() for overlay in overlays):
            return overlays[0]
        else: 
            return None


def navigate(agent,url,website_context,key,user_context):
#   options = uc.ChromeOptions()
#   options=webdriver.ChromeOptions()
#   print("BEFORE CHROME OPTIONS")
#   options.binary_location = os.getenv('GOOGLE_CHROME_BIN')

#   options.add_argument("enable-automation")
#   options.add_argument("--headless")
#   options.add_argument("--window-size=1920,1080")
#   options.add_argument("--no-sandbox")
#   options.add_argument("--disable-extensions")
#   options.add_argument("--dns-prefetch-disable")
#   options.add_argument("--disable-gpu")
#   options.set_capability("pageLoadStrategy", "normal")
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  print("AFTER OPTIONS")

  driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
  
  print("DRIVER BEFORE GETTING")
  driver.get(url)
  print("DRIVER GETTING")
  context=""
  feedback=""
  window_size = driver.get_window_size()
  width = window_size['width']
  height = window_size['height']

  driver.set_window_size(width, height)


#   last_height = driver.execute_script("return document.body.scrollHeight")
#   max_height = driver.execute_script("return document.body.scrollHeight;")
#   print("max height"+ str(max_height))
  counter = 1      
  while counter< 2: 
    time.sleep(4)
    count1=0
    document_height=driver.execute_script("return document.body.scrollHeight")
    current_height=-700
    all_els=[]
    past_height=1
    # all_str=[]
    imgs=[]
    while count1<2 and current_height<document_height-700 and past_height!=current_height: 
        print("loop iteration")
        heihgt=-500
        elslist=get_all_clickable_elements(driver)
        print(str(len(elslist)))
        screenshot= driver.get_screenshot_as_base64()
        driver.save_screenshot(f'screenshots/scroll_{count1*counter}.png')
        imgs.append(screenshot)
        all_els.append(elslist)
        # all_str.append(strlist)
        popup=detect_popup(driver)
        if popup is not None:
            driver.execute_script("""
var popup = arguments[0];
popup.scrollTop += popup.clientHeight;
""", popup)
        else:
            print("POPUP")
            driver.execute_script("window.scrollBy(0, window.innerHeight*1);")
        past_height=current_height
        current_height = driver.execute_script("return window.pageYOffset;")
        print(count1)
        count1+=1
    driver.execute_script("window.scrollBy(0, window.innerHeight*-2);")
    print("Finished looping")
    all_els=[item for sublist in all_els for item in sublist]
    # all_str=[item for sublist in all_str for item in sublist]
    # unique_els=list(set(all_els))
    unique_els = []
    seen_ids = set()
    for el in all_els:
        el_id = el.id  # Get the unique ID of the WebElement
        if el_id not in seen_ids:
            unique_els.append(el)
            seen_ids.add(el_id)

    unique_str= get_texts_of_elements(driver,unique_els)

    totalstr=""
    for stringval in unique_str: 
       stringval=' '.join(stringval.splitlines())
       print("Parent text"+ stringval)
    #    stringval=stringval.strip("\n")
       totalstr+=stringval + "\n"
    
    # print("Clickable elements driver "+ totalstr)
    print("DONE CLICKING")
    flag2=(len(imgs)==2)
    flag3=(len(imgs)==3)
    img2=None
    img3=None
    if flag2 or flag3: 
       img2=imgs[1]
    if flag3: 
       img3=imgs[2]
    img1=imgs[0]
    tup= decode_vision_json(agent.vision_test(key,img1,img2,img3,flag2,flag3,website_context,context,totalstr,user_context))
    print("Length of regular list"+ str(len(all_els)))

    print("Length of unique element list"+ str(len(unique_els)))
    if tup[0]==True: 
       browser_click(tup[1],driver,False,all_els)
       context+=" Button Click: "+ str(tup[1])
       feedback+=tup[2] +"\n"
    else: 
       browser_search(driver,tup[1])
       context+= "Searched up"+ str(tup[1])
       feedback+=tup[2] +"\n"
    counter+=1
    print("Context "+ context)
    print("FEEDBACK"+feedback)
  try: 
      driver.close()
      print("TEST")
  except: 
      print("CLSOED ISSUE")
  return feedback

def chain3( prompt: PromptTemplate) -> LLMChain:
        llm1 = ChatOpenAI(model_name='gpt-3.5-turbo',temperature=0.5,api_key="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")
        return LLMChain(
            llm=llm1, prompt=prompt,
        )

def feedbackprompt(feedback):
    llm = ChatOpenAI(api_key="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", model="gpt-4-1106-preview")

# Langchain prompt
    prompt = PromptTemplate.from_template(f"""
Analyze the following user feedback on a website and provide a detailed analysis, including key insights and important information extracted from the feedback. 

User Feedback: {feedback}

Based on the analysis, evaluate the user's experience in terms of Clarity, Functionality, Usability, and Retention. Provide scores for each category on a scale from 0 to 1, where 1 represents the highest level of satisfaction and 0 the lowest. Return the evaluation in the form of a list with each metric in the order they were presented here.
In this list in the end also return analysis of the user's feedback. Make it in similair length to their feedback and provide detailed analysis of the uesr's pain points and thoughts when interacting with the product. So for example you could return [.65,.43,.81,.92, User feedback here.]. Only return the list. Make sure you only return a list and nothing else.
""")
    response = chain3(prompt).run({}).strip()
    return response

def total_usabillity_test(agent_name,website_context,email,url):
  agent=load_agent_database.LoadAgent(email,agent_name)
  print("BEFORE USER CONTECT")
  questionstring= f"What would you want from a product whose description is this:{website_context}. Think about what features and desings you would want on the software."
  user_context=str(agent.generate_question_response(questionstring))
  print("BEFORE AFTER USER CONTECT")
  feedback=str(navigate(agent,url,website_context,"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",user_context))
  print(feedback)
  finalfeedback=feedbackprompt(feedback)
  return finalfeedback

# print(total_usabillity_test('nick',"A social media platform where users can post about any material",'rbp94@cornell.edu','https://www.reddit.com'))








    
