## 사용방법
# pyperclip을 설치해야 함
# github에서 복사하고 싶은 jupyter notebook의 raw를 클릭한 뒤
# 전체선택해서 ctrl+c로 복사하면
# 파일이 생성됩니다.

# ctrl + c로 복사한 값이 pyperclip.paste()로 전달됨

import time
import pyperclip

현재값 = ""
파일이름 = "20210630"
파일카운트 = 0
while True:
    복사된값 = pyperclip.paste()
    if 현재값 != 복사된값:
        현재값 = 복사된값
        if 파일카운트 != 0:
            with open(f'{파일이름}_{파일카운트}.ipynb', "w", encoding="utf-8") as f:
                f.write(현재값)
        파일카운트 += 1
    time.sleep(0.1)