#!/usr/bin/env python3
"""Hook & CTA Manager — 고효율 후크 및 행동 유도 문구 라이브러리 관리 도구.

이 도구는 작가 에이전트가 축적한 후크와 CTA 데이터를 관리하고 조회합니다.
"""
import os, json, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "hook_library.json")

def load_db():
    if not os.path.exists(DB_PATH):
        return {"hooks": [], "ctas": []}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def main():
    db = load_db()
    
    if len(sys.argv) < 2:
        print("❌ 사용법: python hook_manager.py [list|add_hook|add_cta] [내용]")
        sys.exit(1)

    cmd = sys.argv[1]
    
    if cmd == "list":
        print("─── Hook & CTA 라이브러리 현황 ───")
        print(f"\n[Hook ({len(db['hooks'])}개)]")
        for i, h in enumerate(db['hooks']): print(f"{i+1}. {h}")
        print(f"\n[CTA ({len(db['ctas'])}개)]")
        for i, c in enumerate(db['ctas']): print(f"{i+1}. {c}")

    elif cmd == "add_hook":
        content = " ".join(sys.argv[2:])
        db['hooks'].append(content)
        save_db(db)
        print(f"✅ 후크 추가 완료: {content}")

    elif cmd == "add_cta":
        content = " ".join(sys.argv[2:])
        db['ctas'].append(content)
        save_db(db)
        print(f"✅ CTA 추가 완료: {content}")

    else:
        print(f"❌ 알 수 없는 명령: {cmd}")

if __name__ == "__main__":
    main()
