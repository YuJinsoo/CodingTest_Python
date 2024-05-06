# 52

import subprocess

## encoding 에 utf8 안됨.. 왜? 'cmd', '/c', 
result = subprocess.run(['cmd', '/c', 'echo', '자식 프로세스가 보내는 인사!'],
                        capture_output=True,
                        encoding='cp949')


# 종료코드가 0이 아니면 예외 발생하는 함수.
result.check_returncode()

print(result.stdout)
# print(result.stdout.decode('cp949')) ## euc-kr or cp949



# proc = subprocess.Popen(['powershell', '/c', 'sleep', '1'])
# while proc.poll() is None:
#     print('작업 중...')
    
# print('종료 상태', proc.poll())


# import time
# start = time.time()

# sleep_procs = []

# for _ in range(10):
#     proc = subprocess.Popen(['powershell', '/c', 'sleep', '1'])
#     sleep_procs.append(proc)

# for proc in sleep_procs:
#     proc.communicate()

# end = time.time()

# running_time = end - start
# print(f'{running_time:.3}초 만에 끝남') # 3.58초 만에 끝남

# import os
# import subprocess

# def run_encrypt(data):
#     env = os.environ.copy()
#     env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
#     proc = subprocess.Popen(
#         ['powershell', '/c', 'openssl', 'enc', '-des3', '-pass', 'env:password', '-pbkdf2'],
#         env=env,
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE)
#     out, err = proc.communicate(input=data)
#     if err:
#         print("Error:", err.decode())
#     return out

# results = []

# for _ in range(3):
#     data = os.urandom(10)
#     proc = run_encrypt(data)
#     results.append(proc)

# for result in results:
#     print(result[-10:])

# b'\x8f\x8d\xf7\xb03N\xc3\x1b\xefm'
# b'\xc9dx\xc3\xa0\xe9v\xcb|\x82'
# b'O\xe3\x9d\xce\x9f\xe1\x0eL|\x97'
    

# import subprocess
# proc = subprocess.Popen(['powershell', '/c', 'sleep', '10'])
# try:
#     proc.communicate(timeout=0.1)
# except subprocess.TimeoutExpired:
#     proc.terminate()
#     proc.wait()

# print('종료상태', proc.poll()) # 종료상태 1

import os
import subprocess

def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(
        ['powershell', '/c', 'openssl', 'enc', '-des3', '-pass', 'env:password', '-pbkdf2'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    out, err = proc.communicate(input=data)
    if err:
        print("Error:", err.decode())
    return out


# 월풀해쉬계산
def run_hash(input_stdin):
    p = subprocess.Popen(
        ['powershell', '/c', 'openssl', 'dgst', 'whirlpool', '-binary'],
        # stdin=input_stdin,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    result, _ = p.communicate(input=input_stdin)
    return result

# 데이터를 암호화하는 프로세스 집합 실행
# 함호화된 출력의 해시를 계싼하는 프로세스 집합 실행

encrypt_procs = []
hash_procs = []

for _ in range(3):
    data = os.urandom(100)
    
    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)
    
    hash_proc = run_hash(encrypt_proc)
    hash_procs.append(hash_proc)
    
    # encrypt_proc.stdout.close()
    # encrypt_proc.stdout = None

for p in encrypt_procs:
    print(p[-10:])
    # p.communicate()
    # assert p.returncode == 0

for p in hash_procs:
    print(p[-10:])