from serpapi import GoogleSearch
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import lxml
import requests
import re
import html2text
from serpapi import GoogleSearch
from transformers import pipeline


def scrape_page(link:str):
  try: 
    req = Request(
      url=link, 
      headers={'User-Agent': 'Mozilla/5.0'}
  )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
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




result = [{'position': 1, 'title': 'Basketball Skills Training: 7 Exercises to Improve Jump ...', 'link': 'https://vertimax.com/blog/basketball-skills-training-7-exercises-to-improve-jump-and-agility', 'displayed_link': 'https://vertimax.com › blog › basketball-skills-training...', 'favicon': 'https://serpapi.com/searches/653f212adefa13a6aa26e8f4/images/edfbba356eed760a0ba7e0270388b369190ce1ee038221f0455be01794bada38.png', 'snippet': '7 Basketball Skills Training Exercises · 1. Jump Squats · 2. Tuck Knee Jumps · 3. Overhead Reaching Jump · 4. Single-Legged Cross Jumps · 5. Wall Touches / Cone Taps.', 'snippet_highlighted_words': ['Basketball', 'Jump', 'Jumps', 'Jump', 'Jumps'], 'about_page_link': 'https://www.google.com/search?q=About+https://vertimax.com/blog/basketball-skills-training-7-exercises-to-improve-jump-and-agility&tbm=ilp', 'about_page_serpapi_link': 'https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&q=About+https%3A%2F%2Fvertimax.com%2Fblog%2Fbasketball-skills-training-7-exercises-to-improve-jump-and-agility', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:XKf0FjhfrKgJ:https://vertimax.com/blog/basketball-skills-training-7-exercises-to-improve-jump-and-agility&hl=en&gl=us', 'source': 'Vertimax'}, {'position': 2, 'title': 'How to improve my vertical leap in an effort to be able ...', 'link': 'https://www.quora.com/How-can-I-improve-my-vertical-leap-in-an-effort-to-be-able-to-dunk-a-basketball-Im-61-and-about-180-pounds-but-my-vertical-leap-is-currently-very-poor', 'displayed_link': 'https://www.quora.com › How-can-I-improve-my-vertic...', 'favicon': 'https://serpapi.com/searches/653f212adefa13a6aa26e8f4/images/edfbba356eed760a0ba7e0270388b3697ba0d2a944fd6efe543d3063e914304c.png', 'date': 'Aug 5, 2017', 'snippet': "Decrease your weight, increase your speed, keep your centre of gravity high (don't sink through the hips and shoulders) and keep your eyes focused upwards and ...", 'snippet_highlighted_words': ['increase', 'the'], 'sitelinks': {'list': [{'title': 'How to increase my vertical jump for basketball - Quora', 'link': 'https://www.quora.com/How-do-I-increase-my-vertical-jump-for-basketball', 'answer_count': 16, 'date': 'Dec 12, 2016'}, {'title': 'What is the best way to increase my vertical jump for ...', 'link': 'https://www.quora.com/What-is-the-best-way-to-increase-my-vertical-jump-for-basketball-I-am-6-2-with-shoes-on-and-I-dont-have-access-to-a-gym', 'answer_count': 2, 'date': 'Sep 9, 2018'}, {'title': 'What is the most effective way to increase vertical ...', 'link': 'https://www.quora.com/What-is-the-most-effective-way-to-increase-vertical-jump-for-a-basketball-player-that-already-does-full-time-basketball', 'answer_count': 2, 'date': 'Feb 3, 2018'}, {'title': 'How to increase my vertical jump for basketball within ...', 'link': 'https://www.quora.com/How-can-I-increase-my-vertical-jump-for-basketball-within-a-short-time', 'answer_count': 3, 'date': 'Nov 2, 2016'}]}, 'about_page_link': 'https://www.google.com/search?q=About+https://www.quora.com/How-can-I-improve-my-vertical-leap-in-an-effort-to-be-able-to-dunk-a-basketball-Im-61-and-about-180-pounds-but-my-vertical-leap-is-currently-very-poor&tbm=ilp', 'about_page_serpapi_link': 'https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&q=About+https%3A%2F%2Fwww.quora.com%2FHow-can-I-improve-my-vertical-leap-in-an-effort-to-be-able-to-dunk-a-basketball-Im-61-and-about-180-pounds-but-my-vertical-leap-is-currently-very-poor', 'source': 'Quora'}, {'position': 3, 'title': 'How to Increase Your Vertical Jump (Complete Step by ...', 'link': 'https://www.breakthroughbasketball.com/fitness/increase-vertical-jump.html', 'displayed_link': 'https://www.breakthroughbasketball.com › fitness › in...', 'favicon': 'https://serpapi.com/searches/653f212adefa13a6aa26e8f4/images/edfbba356eed760a0ba7e0270388b3697c582816b31bc66dc807809aff2d64bf.png', 'snippet': "Tip #1: Don't break at the waist. Many athletes underestimate how much the hips affect vertical jump. But tapping into the power of your hips with proper ...", 'snippet_highlighted_words': ['the', 'the', 'vertical jump', 'the'], 'about_page_link': 'https://www.google.com/search?q=About+https://www.breakthroughbasketball.com/fitness/increase-vertical-jump.html&tbm=ilp', 'about_page_serpapi_link': 'https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&q=About+https%3A%2F%2Fwww.breakthroughbasketball.com%2Ffitness%2Fincrease-vertical-jump.html', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:V4NK564jQd4J:https://www.breakthroughbasketball.com/fitness/increase-vertical-jump.html&hl=en&gl=us', 'source': 'Breakthrough Basketball'}, {'position': 4, 'title': 'The Science Behind Your Vertical Leap', 'link': 'https://www.usab.com/news/2015/04/the-science-behind-your-vertical-leap', 'displayed_link': 'https://www.usab.com › news › 2015/04 › the-science...', 'favicon': 'https://serpapi.com/searches/653f212adefa13a6aa26e8f4/images/edfbba356eed760a0ba7e0270388b369d48fc334d65048e94f73fe76706825db.png', 'snippet': 'The most effective way to measure your strength when it comes to the vertical jump is through exercises such as the full Olympic back squat, front squat, power- ...', 'snippet_highlighted_words': ['The', 'the vertical jump', 'the'], 'about_page_link': 'https://www.google.com/search?q=About+https://www.usab.com/news/2015/04/the-science-behind-your-vertical-leap&tbm=ilp', 'about_page_serpapi_link': 'https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&q=About+https%3A%2F%2Fwww.usab.com%2Fnews%2F2015%2F04%2Fthe-science-behind-your-vertical-leap', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:knTUKJ-OvPcJ:https://www.usab.com/news/2015/04/the-science-behind-your-vertical-leap&hl=en&gl=us', 'source': 'USA Basketball'}, {'position': 5, 'title': 'How to Double Your Vertical Jump for Basketball', 'link': 'https://www.basketballforcoaches.com/vertical-jump/', 'displayed_link': 'https://www.basketballforcoaches.com › vertical-jump', 'snippet': 'Slow Motion Squats – 3 sets of 10 repetitions. 5. Lateral Jumps – 3 sets of 20 repetitions. 6. Alternating Jump Lunges – 3 sets of 10 repetitions.', 'snippet_highlighted_words': ['Jumps', 'Jump'], 'about_page_link': 'https://www.google.com/search?q=About+https://www.basketballforcoaches.com/vertical-jump/&tbm=ilp', 'about_page_serpapi_link': 'https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&q=About+https%3A%2F%2Fwww.basketballforcoaches.com%2Fvertical-jump%2F', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:E88E-HkEdtEJ:https://www.basketballforcoaches.com/vertical-jump/&hl=en&gl=us', 'missing': ['performance'], 'must_include': {'word': 'performance', 'link': "https://www.google.com/search?sca_esv=577697702&q=''How+can+I+increase+my+vertical+jump+for+better+basketball+%22performance%22+?'&sa=X&ved=2ahUKEwjCrsi-6JyCAxVST6QEHSTGCdoQ5t4CegQINhAB"}, 'source': 'Basketball for Coaches'}, {'position': 6, 'title': "Sean Conaty brings the 'juice' to Mizzou Basketball", 'link': 'https://missouri.rivals.com/news/sean-conaty-brings-the-juice-to-mizzou-basketball', 'displayed_link': 'https://missouri.rivals.com › news › sean-conaty-bring...', 'favicon': 'https://serpapi.com/searches/653f212adefa13a6aa26e8f4/images/edfbba356eed760a0ba7e0270388b369198cbe38810b230b032cafdeb0ce16d7.png', 'date': '8 days ago', 'snippet': "A year ago, the forward used them as a reference point to show off his max vertical leap of 49 inches — a mark that would've broken the NBA ...", 'snippet_highlighted_words': ['the', 'his', 'vertical leap', 'the'], 'about_page_link': 'https://www.google.com/search?q=About+https://missouri.rivals.com/news/sean-conaty-brings-the-juice-to-mizzou-basketball&tbm=ilp', 'about_page_serpapi_link': 'https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&q=About+https%3A%2F%2Fmissouri.rivals.com%2Fnews%2Fsean-conaty-brings-the-juice-to-mizzou-basketball', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:Yjyrht4QQhQJ:https://missouri.rivals.com/news/sean-conaty-brings-the-juice-to-mizzou-basketball&hl=en&gl=us', 'source': 'PowerMizzou'}, {'position': 7, 'title': 'Clinical EFT Handbook Volume 2 - Volume 2 - Google Books Result', 'link': "https://books.google.com/books?id=xydnDwAAQBAJ&pg=PT210&lpg=PT210&dq=''How+can+I+increase+my+vertical+jump+for+better+basketball+performance?'&source=bl&ots=EcjXUob7eb&sig=ACfU3U20aAN0q-mp3b0u8qy8S7gV1NjrTQ&hl=en&sa=X&ved=2ahUKEwjCrsi-6JyCAxVST6QEHSTGCdoQ6AF6BAgjEAM", 'displayed_link': 'https://books.google.com › books', 'snippet': 'Dawson Church, Stephanie Marohn. A basic requirement of good research is that the ... jump height. When performance was analyzed separately by gender, trends ...', 'snippet_highlighted_words': ['good', 'the', 'jump', 'performance'], 'rich_snippet': {'top': {'extensions': ['Dawson Church, \u200eStephanie Marohn', '2013', '\u200ePsychology'], 'detected_extensions': {'unknown': 2013}}}, 'source': 'google.com'}]
 
# print(scrape_page('https://www.quora.com/How-can-I-improve-my-vertical-leap-in-an-effort-to-be-able-to-dunk-a-basketball-Im-61-and-about-180-pounds-but-my-vertical-leap-is-currently-very-poor'))
# for page in result:
#   print(page['link'] +"\n")

#   print("Article text\n"+"-"+str(scrape_page(page['link'])))

def scrape_pages_list(urlslist):
  final_text_list=[]
  for url in urlslist:
    text=scrape_page(url)
    text_split= text.split(" ")
    if len(text_split)>25: 
      final_text_list.append(text)
  return final_text_list
      
def summarize(text):
  summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")
  text=summarizer(text)
  return text[0]['summary_text']

def get_words_in_batches(text):
    words = text.split()
    num_batches = len(words) // 600

    batches = []
    for i in range(num_batches):
        start = i * 600
        end = start + 600
        batch = ' '.join(words[start:end])
        batches.append(batch)

    return batches

def summarize_batches(text):
   batches=get_words_in_batches(text)
   finalstring=""
   for batch in batches: 
    finalstring+=str(summarize(batch))
   return finalstring

def api_results(query): 

  params = {
    "engine": "google",
    "q": query,
    "api_key": "2a1b3c69c495a34d2328c393b729f971563d489b464266a90fcb0bd214ce452f"
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  organic_results = results["organic_results"]
  urllist=[]
  for page in organic_results: 
    urllist.append(page["link"])
  return urllist

# print(api_results("Home Financing"))

def urls_to_summarizedtext(urllist): 
  scraped_lists=scrape_pages_list(urllist)
  print(scraped_lists)
  new_list=[]
  for text in scraped_lists: 
    text1=""
    if (len(text.split())>1500): 
      count=0
      for word in text.split(): 
        if count>1300:
          break 
        else:
          text1+=" "+ word
          count+=1
    new_list.append(summarize_batches(text1))
  return new_list


