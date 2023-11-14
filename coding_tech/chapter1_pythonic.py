# 1
# import sys
# print(sys.version_info) 
# # sys.version_info(major=3, minor=9, micro=13, releaselevel='final', serial=0)
# print(sys.version)
# # 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]


# 1-3
# a = b'h\x65llo'
# print(list(a))  # [104, 101, 108, 108, 111]
# print(a)        # 


# a = 'a\u0300 propos'
# print(list(a))
# print(a)

# def to_str(bytes_or_str):
#     if isinstance(bytes_or_str, bytes):
#         value = bytes_or_str.decode('utf-8')
#     else:
#         value = bytes_or_str
#     return value

# print(repr(to_str(b'foo')))
# print(repr(to_str('bar')))
# print(repr(to_str(b'\xed\x95\x9c')))

# def to_bytes(bytes_or_str):
#     if isinstance(bytes_or_str, str):
#         value = bytes_or_str.encode('utf-8')
#     else:
#         value = bytes_or_str
#     return value

# print(repr(to_bytes(b'foo')))             #'foo'
# print(repr(to_bytes('bar')))              #'bar'
# print(repr(to_bytes('한글')))             #'한'

# # with open('data.bin', 'w') as f:
# #     f.write(b'\xf1\xf2\xf3\xf4\xf5') ## 에러

# with open('data.bin', 'wb') as f:
#     f.write(b'\xf1\xf2\xf3\xf4\xf5') ## 실행됨

# # # 저장된것 열때
# # with open('data.bin', 'r') as f:
# #     data = f.read() ## 에러

# with open('data.bin', 'rb') as f:
#     data = f.read() ## 실행됨
#     print(data) # '\xf1\xf2\xf3\xf4\xf5 '

# with open('data.bin', 'r', encoding='cp1252') as f:
#     data = f.read() ## 실행됨
#     print(data) # ñòóôõ

# ## 문자열을 encode하면 ascii 값과 같은 binary 값을 가짐
# char = 'a'
# binary_char = char.encode()
# print(char)                 # a
# print(binary_char)          # b'a'
# print(binary_char[0])       # 97
# print(bin(binary_char[0]))  # 0b1100001
# print(hex(binary_char[0]))  # 0x61

# 1-4
# a = 0b10111011
# b = 0xc5f
# print('이진수: %d, 십육진수: %d' % (a,b))


# key = 'my_car'
# value = 1.234
# formatted = '%-10s = %.2f' % (key, value)
# print(formatted) #

# pantry = [
#     ('아보카도', 1.25),
#     ('바나나', 2.50),
#     ('사과', 15.00),
#     ]

# for i, (item, count) in enumerate(pantry):
#     print('#%d: %-10s = %.2f' % (i, item, count))

# # 위 값을 다르게 수정하고 싶을 때
# for i, (item, count) in enumerate(pantry):
#     print('#%d: %-10s = %d' % (i+1, item.title(), round(count)))

# a = 1234.5678
# formatted = format(a, ',.2f')
# print(formatted)
# # 1,234.57

# b = 'my문자열'
# formatted = format(b, '^20s')
# print('*', formatted, '*')
# # *        my문자열         *

# key = 'my_var'
# value = 1.234
# formatted = '{} = {}'.format(key, value)
# print(formatted) # my_var = 1.234

# formatted = '{:<10} = {:.2f}'.format(key, value)
# print(formatted) # my_var     = 1.23


# print('{} replaces {{}}'.format(1.23))
# print('%.2f%%' % 12.5)

# key = 'my_var'
# value = 1.234
# formatted= '{1} = {0}'.format(key, value)
# print(formatted) # 1.234 = my_var

# formatted = '{1} = {1} = {1}'.format(key, value)
# print(formatted) # 1.234 = 1.234 = 1.234

# key = 'my_var'
# value = 1.234
# formatted = f'{key} = {value}'
# print(formatted) # my_var = 1.234

# formatted = f'{key!r:<10} = {value:.2f}'
# print(formatted) # 'my_var'   = 1.23

# f_string = f'{key:<10} = {value:.2f}'
# c_type = '%-10s = %.2f' % (key, value)
# str_format = '{:<10} = {:.2f}'.format(key, value)
# str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)
# c_dict = '%(key)-10s = %(value).2f' % {'key':key, 'value':value}

# assert c_type == c_dict == f_string
# assert str_format == str_kw == f_string

# places = 3
# number = 1.234567
# print(f'내가 고른 숫자는 {number:.{places}f}') # 내가 고른 숫자는 1.235

# 1-5

from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=', keep_blank_values=True)
print(repr(my_values)) # {'빨강': ['5'], '파랑': ['0'], '초록': ['']}

red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0
print(f"빨강:{red!r}")
print(f"초록:{green!r}")
print(f"투명도:{opacity!r}")
# 빨강:'5'
# 초록:0
# 투명도:0

