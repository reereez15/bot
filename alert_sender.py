import requests
import json
import random

# n8n Webhook 프로덕션(또는 테스트) URL
# ※ 실서비스 자동 실행 시에는 webhook 뒤에 -test가 없는 Production URL을 쓰는 것이 일반적입니다.
WEBHOOK_URL = "http://localhost:5678/webhook/security-alert"

# 임의의 테스트 IP 목록
IP_POOL = ["1.2.3.114", "192.168.0.10", "10.0.0.5", "203.0.113.195"]
RULES = ["5712", "1001", "3110", "4002"]

payload = {
    "student": "홍길동",  # 본인 이름/학번
    "alerts": [
        {
            "ip": random.choice(IP_POOL),
            "level": random.choice([3, 5, 7, 10, 12]),
            "rule": random.choice(RULES)
        }
    ]
}

try:
    headers = {"Content-Type": "application/json; charset=utf-8"}
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers, timeout=5)
    print(f"[+] Alert 전송 완료: {response.status_code} - {response.text}")
except Exception as e:
    print(f"[-] 전송 실패: {e}")