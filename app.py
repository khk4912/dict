from flask import *
from flask_compress import Compress
import os
from bs4 import BeautifulSoup
import requests
import random

with open("words.txt", "r") as f:
    word_list = f.read().splitlines()

word_list = [i.lower() for i in word_list]


compress = Compress()
app = Flask(__name__)
app.secret_key = os.urandom(15)
compress.init_app(app)


@app.route('/')
def index():
    return render_template("index.html", count=len(word_list))


@app.route('/search', methods=['POST'])
def search():
    word = request.form['search']
    if word.strip() in word_list:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Mobile Safari/537.36"
            }
            r = requests.get(
                "https://endic.naver.com/search.nhn?sLn=kr&query=%s&searchOption=entryIdiom" % (word), headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            word = soup.find_all("div",{"class":"h_word _tipSkipItem"})[0].find("strong").text
            mean = soup.find_all("p",{"class":"desc"})[0].text
        except:
            mean = "네이버 사전에 뜻이 없음!"
        return render_template("search.html", word=word, mean=mean)
    else:
        flash("서버에 없는 단어입니다!")
        return redirect(url_for("index"))

@app.route('/random_search', methods=['POST'])
def random_search():
    word = random.choice(word_list)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Mobile Safari/537.36"
        }
        r = requests.get(
            "https://endic.naver.com/search.nhn?sLn=kr&query=%s&searchOption=entryIdiom" % (word), headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        word = soup.find_all("div",{"class":"h_word _tipSkipItem"})[0].find("strong").text
        mean = soup.find_all("p",{"class":"desc"})[0].text
    except:
        mean = "네이버 사전에 뜻이 없음!"
    return render_template("search.html", word=word, mean=mean)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", threaded=True, port=80)
