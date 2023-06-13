## 사용방법
# pyperclip을 설치해야 함
# 엑셀에서 값을 ctrl + c로 복사한 뒤 이 파일을 실행하면
# data에서 복사한 값을 확인할 수 있습니다.

# ctrl + c로 복사한 값이 pyperclip.paste()로 전달됨


import time
import pyperclip

복사된값 = pyperclip.paste()
data = [value for value in 복사된값.split('\r\n') if value]
print(data)

#python 002_excelcopy.py
# ['1', '2', '3', '4', 'a', 'abd']

# 왜 ctrl + F5로 실행할땐 No module named 'pypyerclip' 뜨는거지..?
# https://velog.io/@sicksong/ERROR-VSCode-python-library-pyperclip-import-%EC%97%90%EB%9F%AC