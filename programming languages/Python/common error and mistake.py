### Những lỗi có thể gặp khi lập trình với python

## 1. Thay đổi giá trị của một đối tượng immutable

s = 'string'    # s (kiểu str) là một đối tượng immutable
s[2] = 'o'      # Không thể thay đổi giá trị. Báo lỗi "TypeError"

## 2. Thực hiện cộng trừ giữa chuỗi và số

age = 36
txt = "My name is J, I am " + age

