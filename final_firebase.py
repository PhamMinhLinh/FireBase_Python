import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
# Khởi tạo Firebase App và Database Reference
cred = credentials.Certificate("argon-radius-377619-firebase-adminsdk-3h1cn-0e3b3095f7.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://argon-radius-377619-default-rtdb.firebaseio.com/'})
ref = db.reference('random_number')
# Định nghĩa callback function
def on_update(event):
    print('New value:', event.data)
# Đăng ký callback function với database reference
ref.listen(on_update)
# Tạo số ngẫu nhiên từ 1 đến 10 và cập nhật liên tục lên Firebase
while True:


    my_list = [-100, 100]
    random_element = random.choice(my_list)

    print(random_element)

    # rand_num = random.randint(-100, 100)
    ref.set(random_element)
    time.sleep(2)