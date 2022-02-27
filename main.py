import flask 
import re
import urllib.request
import requests
import json, random, string
from bs4 import BeautifulSoup as bs

from config import PORT
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home_page():
    for i in range(1,2):
        page_number = (i)
        length = int(5) 
        upper = string.ascii_lowercase
        data = random.sample(upper,length)
        parser = "".join(data)
        search_keyword = parser
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        Video_Link = "https://www.youtube.com/watch?v=" + video_ids[1]

        r = requests.get(Video_Link)
        soup = bs(r.content, 'lxml')
        new = soup.select_one('title').text
        Title = new[:-10]
        new_string = ''
        for char in Title:
            if char != '"' and char != "'":
              new_string +=char
#uncomment if you do not need emojis in the youtube video title

#         def deEmojify(new_string):
#             regrex_pattern = re.compile(pattern = "["
#                 u"\U0001F600-\U0001F64F"
#                 u"\U0001F300-\U0001F5FF" 
#                 u"\U0001F680-\U0001F6FF" 
#                 u"\U0001F1E0-\U0001F1FF"  
#                 u"\U00002702-\U000027B0"
#                 u"\U000024C2-\U0001F251"
#                 u"\U0001f926-\U0001f937"      
#                 u'\U00010000-\U0010ffff'
#                 u"\u200d"
#                 u"\u2640-\u2642"
#                 u"\u2600-\u2B55"
#                 u"\u23cf"
#                 u"\u23e9"
#                 u"\u231a"
#                 u"\u3030"
#                 u"\ufe0f"
#                             "]+", flags = re.UNICODE)
#             return regrex_pattern.sub(r'',new_string)
#         Video_Name = deEmojify(new_string)

          Video_Name = new_string

    def main():
       (Video_Name,Video_Link)
    data = {}
    data = {
        "Video_Title":Video_Name, 
        "Video_Link":Video_Link
    }
    New_Data = str(json.dumps(data))
    main()
    with open("data.json", "w") as file:
       file.write(f"[{New_Data}]")
       file.write("\n") 
       json_dump = data
       return json_dump

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
