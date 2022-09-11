import os 


# /Users/kimuratoshiyuki/Dropbox/Python/hayatas-Udemy_スクレイピング/selenium/実用的なパスの書き方/lesson.py
print(os.path.abspath(__file__))

# /Users/kimuratoshiyuki/Dropbox/Python/hayatas-Udemy_スクレイピング/selenium/実用的なパスの書き方
dir_name = os.path.dirname(os.path.abspath(__file__))

print(os.path.join(dir_name, 'html', 'index.html'))