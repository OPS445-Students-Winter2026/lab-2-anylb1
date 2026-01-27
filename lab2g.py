#!/usr/bin/env python3
# Author: Fonkouop Bless Anyl
# Author ID: 121208235
# Date Created: 2026/01/27

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")
