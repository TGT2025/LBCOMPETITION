# 🎯 LB Competition JUNE 2025 – Draw System

This repo contains the **official provably fair draw system** used for the LB JUNE 2025 Competition.

---

## 🧾 How the Draw Works

Every order marked **`sent`** between:

```
🗓️ 15 April → 1 June 2025 
```

…is entered into the competition.

The draw is based on:
- A **public timestamp string**
- SHA256 hash of that string
- Random generator seeded with the hash
- 5 winners randomly selected from `entries.txt`

---

## 🔐 Fairness Protocol

This repo is public and timestamped.  
No changes will be made to the draw code.

On **1 June 2025**:
- We will publish the full `entries.txt` list of order numbers
- We will publish the **timestamp string** used
- Anyone can run the script and verify the same result

---

## 🎯 Files

| File          | Purpose                                      |
|---------------|-----------------------------------------------|
| `draw.py`     | The official drawing script                   |
| `entries.txt` | *(Will be uploaded on draw day)* Eligible `sent` orders |

---

## 🧪 How to Verify

1. Download this repo
2. Open terminal or PowerShell
3. Run:

   python draw.py

4. When prompted, enter:

   LB DRAW JUNE 2025

5. You’ll get the **same winners we posted**

---

## 🏆 What This Guarantees

- ✅ You see the full list used
- ✅ You see the exact script used
- ✅ You see the public timestamp
- ✅ You can reproduce the result
- ✅ Nobody can cheat, edit, or change the outcome

This is the highest standard of fairness in community draws.

