from pathlib import Path

required = ["AGENTS.md", "README.md", "config", "agents", "skills", "workflows"]
missing = [x for x in required if not Path(x).exists()]

if missing:
    print("누락:", ", ".join(missing))
    raise SystemExit(1)

print("기본 구조 확인 완료")
