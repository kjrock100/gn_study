#!/usr/bin/env python3


import os, sys

# 현재 작업 디렉토리 출력
print("현재 디렉토리:", os.getcwd())
print("전체 인자:", sys.argv)


# version.py
with open(sys.argv[1]) as f:
    print(f.read().strip())
