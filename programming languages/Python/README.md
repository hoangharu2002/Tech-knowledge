# Overview

- Guido van Rossum
- 1991
- Python 2 -> Python 3

- Chạy file script dưới dạng module: "python -m [filename]"
- Tạo môi trường ảo: "python -m venv|virtualenv [virtual_folder_name]"
- Hàm thoát 'exit()' trong python thường được thêm tự động bởi module 'site', trường hợp không dùng module 'site' hệ thống sẽ báo lỗi, sửa lỗi bằng cách "sys.exit()" hoặc "raise SystemExit()"
- Sử dụng @decorator để thay đổi hoặc mở rộng một hàm đã có mà không cần phải thay đổi code của nó. Một số decorator: @property, @classmethod, @staticmethod...
- Những thực thi mang tính hệ thống nên được xử lý bên trong hàm main(), không nên được xử lý bên trong các hàm cục bộ.

## Thư viện

- 'Six'(?): thư viện hỗ trợ viết mã tương thích cho Python2 và Python3.
- 'sys': thư viện hệ thống.
- 'argparse'(*): thư viện mạnh mẽ để xử lý các đối số dòng lệnh (command line).
- 'pytest'(*): công cụ kiểm thử, thư viện hỗ trợ viết unit tests và kiểm soát exception.
- 'mypy': công cụ kiểm tra các lỗi liên quan đến khai báo và sử dụng kiểu dữ liệu, thư viện cung cấp khả năng tạo các nhãn kiểu dữ liệu một cách linh hoạt.
- 'site': module mặc định khi làm việc với python, được thêm vào tự động mỗi khi thực thi trong môi trường python bình thường, có chức năng thêm vào các cấu hình ban đầu cũng như thêm vào các hàm, thư viện... và set up đường dẫn tới các thư viện của hệ thống.
- 'functools': module được tích hợp sẵn trong python, cung cấp các công cụ tiện ích cho việc xử lý và thao thác với các hàm.
- 'pprint': module hỗ trợ việc in các cấu trúc dữ liệu phức tạp được gọn gàng và đẹp hơn.
** Chú thích: Dấu (*) thể hiện package được hỗ trợ bởi bên thứ ba. Dấu (?) thể hiện những package chưa được thử nghiệm.

## Tools

- [pip](..\frameworks\pip.md): trình quản lý gói cho python, hỗ trợ cài đặt các gói từ PyPI (Python Package Index - một kho lưu trữ trực tuyến các gói phần mềm Python)

## Basic functions

- dir(): liệt kê các thành phần (thuộc tính, phương thức,...) của một module hoặc một đối tượng.
- sorted(): sắp xếp lại các giá trị trong một đối tượng.

## Standar objects

- 'capsys': đối tượng nhận các giá trị được xuất ra màn hình
- '*args': đối tượng cho phép truyền số lượng đối số đơn lẻ chưa xác định
- '**kwargs': đối tượng cho phép truyền số lượng đối số dạng key-value chưa xác định
