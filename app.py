from flask import Flask, render_template
from bs4 import BeautifulSoup
import random
import time

app = Flask(__name__)

# Định nghĩa route mặc định
@app.route('/')
def index():
    return render_template('index.html')

# Định nghĩa route để cập nhật độ ẩm
@app.route('/humidity')
def humidity():
    # Tạo HTML ban đầu
    html = '<h3 id="card-humidity">0</h3>'

    # Phân tích cú pháp HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Vòng lặp vô hạn để cập nhật liên tục độ ẩm
    while True:
        # Tạo giá trị độ ẩm ngẫu nhiên từ 0 đến 100
        humidity = random.randint(0, 100)

        # Cập nhật nội dung của thẻ HTML
        humidity_str = str(humidity)
        humidity_tag = soup.find('h3', id='card-humidity')
        humidity_tag.string = humidity_str

        # Lấy HTML đã được cập nhật và trả về cho trình duyệt
        updated_html = soup.prettify()
        yield updated_html

        # Đợi 1 giây trước khi cập nhật lại giá trị độ ẩm
        time.sleep(1)


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False)