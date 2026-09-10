import math

def calculator(expression: str):
    allowed = {"abs": abs, "round": round, "sqrt": math.sqrt}
    return eval(expression, {"__builtins__": {}}, allowed)

def search_policy(keyword: str):
    policy = {
        "security": "API key는 환경변수에 저장하고 공개 저장소에 커밋하지 않습니다.",
        "license": "사용 데이터의 출처와 라이선스를 README에 기록합니다.",
        "evaluation": "평가셋을 고정하고 동일 조건에서 반복 측정합니다."
    }
    return policy.get(keyword.lower(), "해당 정책을 찾지 못했습니다.")
