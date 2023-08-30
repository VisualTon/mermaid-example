time = "2023/8/25 16:18:20"
status = "Success"
str1 = "Crypto Bot"
str2 = "Canfly's Tonkeeper Wallet"

mermaid_code = f"""
```mermaid
---
title: {time} ({status})
---
flowchart LR
    A("{str1}")
    B("{str2}")
    A -- 0.01 TON --> B
```
"""
print(mermaid_code)
