
### [PCCP 기출문제] 1번 / 붕대 감기
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/250137

```python
## 내풀이 60점... 보완필요
def solution(bandage, health, attacks):
    now = 0
    now_health = health

        
    while attacks:
        heal = 0
        att = attacks.pop(0)
        dur = att[0] - now
        
        ## 회복
        if now_health == health:
            heal = 0
        else:
            heal = (bandage[1] * dur) + (dur//bandage[0] * bandage[2])
            
        if (now_health + heal) > health:
            now_health = health
        
        ## 시간 초기화
        now = att[0]
        
        ## 공격받음
        now_health = now_health - att[1]
        
        if now_health <= 0:
            return -1
                
    return now_health
    
## 남의풀이
def solution(bandage, health, attacks):
    n = max(attacks)[0]

    t, x, y = bandage
    current_health, healing, casting = health, 0, 0

    for i in range(1, n + 1):
        healing += 1
        casting += 1

        # 공격 받을시 체력 차감 및 스킬 재시전
        for attack in attacks:
            if attack[0] == i:
                current_health -= attack[1]
                healing, casting = 0, 0

        # 캐릭터가 죽으면 -1 반환
        if current_health <= 0:
            return -1

        # 공격 받지 않았을 때만 체력 회복
        if healing != 0 and casting != 0:
            current_health += x

        # 추가 회복량만큼 체력 회복
        if casting == t:
            current_health += y

        # 시전 시간이 끝나면 재시전
        if healing == t:
            healing, casting = 0, 0

        # 최대 체력만큼 회복 불가
        if current_health > health:
            current_health = health

    answer = current_health
    return answer
```