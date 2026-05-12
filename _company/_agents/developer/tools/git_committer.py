#!/usr/bin/env python3
"""Git Committer — 작업 단위 자동 커밋 도구.

이 도구는 현재 프로젝트의 변경 사항을 스테이징하고 커밋합니다.
설정 파일(git_committer.json)에서 기본 메시지 규칙을 가져옵니다.
"""
import os, json, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(HERE, "git_committer.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {"DEFAULT_MSG": "chore: update code", "AUTO_STAGE": True}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def run_git(args):
    try:
        result = subprocess.run(["git"] + args, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 오류: {e.stderr}")
        return None

def main():
    cfg = load_config()
    msg = sys.argv[1] if len(sys.argv) > 1 else cfg.get("DEFAULT_MSG")
    
    print("─── Git Committer 실행 중 ───")
    
    # 1. 상태 확인
    status = run_git(["status", "--short"])
    if not status:
        print("✅ 커밋할 변경 사항이 없습니다.")
        return

    print(f"📝 변경 사항 감지:\n{status}")

    # 2. 스테이징
    if cfg.get("AUTO_STAGE"):
        print("🚀 스테이징 중 (git add .)...")
        run_git(["add", "."])

    # 3. 커밋
    print(f"💾 커밋 중: \"{msg}\"")
    result = run_git(["commit", "-m", msg])
    if result:
        print(f"✅ 커밋 성공!")
        print(result)

if __name__ == "__main__":
    main()
