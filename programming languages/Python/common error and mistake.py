### Những lỗi có thể gặp khi lập trình với python

## 1. Thay đổi giá trị của một đối tượng immutable

s = 'string'    # s (kiểu str) là một đối tượng immutable
s[2] = 'o'      # Không thể thay đổi giá trị. Báo lỗi "TypeError"

# Cách fix: tạo thêm một đối tượng lưu trữ mới và xử lý trên đối tượng đó thay vì đối tượng gốc.

## 2. Thực hiện cộng trừ giữa chuỗi và số

age = 36
txt = "My name is J, I am " + age   # không thể thực hiện pháp tính cộng. Báo lỗi "TypeError"

# Cách fix: để kết hợp giữa chuỗi và số, có thể sử dụng f-String hoặc phương thức format() hoặc truyền lần lượt các tham số vào hàm nếu được

