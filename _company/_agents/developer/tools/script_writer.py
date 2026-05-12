#!/usr/bin/env python3
"""Script Writer — 세션 기반 코드 저장 도구.

에이전트 간 논의가 기록된 최신 세션 폴더를 찾아 파이썬(.py) 파일을 저장합니다.
"""
import os, json, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(HERE, "script_writer.json")
# 세션 루트 경로 (고정)
SESSIONS_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "sessions"))

def get_latest_session():
    """가장 최근에 생성된 세션 폴더 경로를 반환합니다."""
    if not os.path.exists(SESSIONS_ROOT):
        return None
    
    # 세션 폴더 패턴: YYYY-MM-DDTHH-MM
    folders = [f for f in os.listdir(SESSIONS_ROOT) if os.path.isdir(os.path.join(SESSIONS_ROOT, f))]
    if not folders:
        return None
        
    # 이름 순으로 정렬 (타임스탬프 형식이므로 마지막이 최신)
    folders.sort()
    return os.path.join(SESSIONS_ROOT, folders[-1])

def main():
    if len(sys.argv) < 3:
        print("❌ 사용법: python script_writer.py [파일명] [코드내용]")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        filename += ".py"
    code_content = sys.argv[2]

    # 세션 폴더 결정
    target_dir = get_latest_session()
    if not target_dir:
        print("❌ 세션 폴더를 찾을 수 없습니다. (경로 확인: {SESSIONS_ROOT})")
        sys.exit(1)

    target_path = os.path.join(target_dir, filename)

    print(f"─── Script Writer (Session Mode) ───")
    print(f"📁 세션 저장 위치: {target_path}")

    try:
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(code_content)
        print(f"✅ 세션 내 파일 저장 성공! ({len(code_content)} bytes)")
    except Exception as e:
        print(f"❌ 저장 실패: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
