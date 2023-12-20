from serpapi import GoogleSearch
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import lxml
import requests
import re
import html2text
from serpapi import GoogleSearch
from transformers import pipeline
from time import sleep
from wrapt_timeout_decorator import *
import threading
import time

from concurrent.futures import ThreadPoolExecutor
from langdetect import detect

def scrape_page(link:str):
  try: 
    req = Request(
      url=link, 
      headers={'User-Agent': 'Mozilla/5.0'}
  )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser',from_encoding="iso-8859-1")
    # text = soup.find_all(text=True)
    # newtext=soup.find_all('p')
    # titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6','p'])
    # titles=re.sub(r'<.*?>', '', str(titles))
    text = soup.get_text()
    h = html2text.HTML2Text()
    h.ignore_links = True
    return h.handle(text)
  except Exception as e:
    return ""




 
# print(scrape_page('https://www.quora.com/How-can-I-improve-my-vertical-leap-in-an-effort-to-be-able-to-dunk-a-basketball-Im-61-and-about-180-pounds-but-my-vertical-leap-is-currently-very-poor'))
# for page in result:
#   print(page['link'] +"\n")

#   print("Article text\n"+"-"+str(scrape_page(page['link'])))

def scrape_pages_list(urlslist):
  final_text_list=[]
  for url in urlslist:
    task_thread = threading.Thread(target=scrape_page, args=(url,))
    task_thread.start()
    task_thread.join(timeout=4)
    if task_thread.is_alive():
      continue
    else:
      text=scrape_page(url)
      text_split= text.split(" ")
      if len(text_split)>0: 
        if is_english(text):
          final_text_list.append(text)

  print('finished iterate')
  return final_text_list
      
def summarize(text):
  # summarizer = pipeline("summarization", model="Falconsai/text_summarization")
  # text=summarizer(text, max_length=500, min_length=200, do_sample=False)
  # return text[0]['summary_text']
  text=str(text)
  return text[:300]

def get_words_in_batches(text):
    text=str(text)
    words = text.split()
    print("afterword")
    num_batches = len(words) // 1300
    print("before loop")
    batches = []
    for i in range(num_batches):
        print("in loop")
        start = i * 1300
        end = start + 1300
        batch = ' '.join(words[start:end])
        batches.append(batch)

    return batches

def summarize_batches(text):
   print("here")
   batches=get_words_in_batches(text)
   print("batches made")
   finalstring=""
   for batch in batches: 
    print("batchx")
    finalstring+=str(summarize(batch))
   return finalstring

def api_results(query): 
  try:
    params = {
        "engine": "google",
        "q": query,
        "api_key": "2a1b3c69c495a34d2328c393b729f971563d489b464266a90fcb0bd214ce452f"
      }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    organic_results = results["organic_results"]
    urllist=[]
    for page in organic_results: 
      urllist.append(page["link"])
    return urllist
  except:
    []

def split_list(lst,num):
    n = len(lst) // num
    return [lst[i * n:(i + 1) * n] for i in range(num)]

def urls_to_summarizedtext(urllist): 
  scraped_results= threaded_scrape(urllist)
  scraped_results1=[element for sublist in scraped_results for element in sublist]
  print("length of scraped results:" + str(len(scraped_results1)))
  split_scraped=split_list(scraped_results1,2)
  print("starting")
  # split_list1= split_list(scraped_paged_list)


  # firstlist=split_list[0]
  # secondlist=split_list[1]
  # thirdlist=split_list[2]
  # fourthlist=split_list[3]
  # first_thread = threading.Thread(target=scrape_and_summarize, args=(firstlist,))
  # second_thread=threading.Thread(target=scrape_and_summarize, args=(secondlist,))
  # third_thread= threading.Thread(target=scrape_and_summarize,args=(thirdlist,) )
  # fourth_thread= threading.Thread(target=scrape_and_summarize, args=(fourthlist,))
  results= scrape_and_summarize(scraped_results1)
  print("result finished")
  print("resultfinished")
  # with ThreadPoolExecutor(max_workers=2) as executor:
  #   # Submit the function to the executor with different arguments
  #   futures = [executor.submit(scrape_and_summarize, arg) for arg in split_scraped]

  #   # Wait for all threads to complete and get results
  #   results = [future.result() for future in futures]

  #   # Wait for completion
  return results
  # print("Results"+str(results))




def scrape_and_summarize(urllist):
  print("length of scraped results:" + str(len(urllist)))
  newlist=[]
  print("thread")
  for text in urllist: 
    text=str(text)
    print("scraping")
    text1=text
    print("change")
    if (len(text.split())>1500): 
      print("if condition")
      text1=text[:4000]
    print("before call")
    newlist.append(summarize_batches(text1))
  return newlist

def threaded_scrape(urllist): 
  split_list1= split_list(urllist,2)
  with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(scrape_pages_list, arg) for arg in split_list1]
    results = [future.result() for future in futures]
    
  return results


def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False
    




def related_questions(query):
  params = {
    "engine": "google",
    "q": query,
    "api_key": "2a1b3c69c495a34d2328c393b729f971563d489b464266a90fcb0bd214ce452f"
  }
  search = GoogleSearch(params)
  results = search.get_dict()
  return results




