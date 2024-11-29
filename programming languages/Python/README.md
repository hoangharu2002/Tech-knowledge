# Overview

- Guido van Rossum
- 1991
- Python 2 -> Python 3

## Data types

- Text type: `str`
      - Methods: *upper()*, *lower()*, *strip()*, *replace()*, *split()*, *join()*, *find()*, capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(), format(), format_map(), index(), isalnum(), *isalpha()*, isascii(), isdecimal(), isdigit(), isidentifier(), *islower()*, isnumeric(), isprintable(), istitle(), *isupper()*, ljust(), *lstrip()*, maketrans(), partition(), *rfind()*, rindex(), rjust(), rpartition(), *rsplit()*, *rstrip()*, splitlines(), startswith(), swapcase(), title(), translate(), zfill(), *isspace()*
- Numeric types: `int`, `float`, `complex`
- Sequence types: `list`, `tuple`, `range`
      - `list`
            - Methods: append(), insert()
- Mapping types: `dict`
- Set types: `set`, `frozenset`
- Boolean type: `bool`
- Binary types: `bytes`, `bytearray`, `memoryview`
- None types: `NoneType`

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
- 'unicodedata': hỗ trợ mã unicode

## Tools

- [pip](..\frameworks\pip.md): trình quản lý gói cho python, hỗ trợ cài đặt các gói từ PyPI (Python Package Index - một kho lưu trữ trực tuyến các gói phần mềm Python)

## Basic functions

- dir(): liệt kê các thành phần (thuộc tính, phương thức,...) của một module hoặc một đối tượng.
- sorted(): sắp xếp lại các giá trị trong một đối tượng.
- type(): trả về kiểu dữ liệu của đối tượng
- print(): hàm dùng để xuất output
- len(): trả về độ dài của một iterator
- ord(): trả về giá trị ASCII của một ký tự
- chr(): trả về ký tự tương ứng với mã ASCII
- range():
- enumerate():
- all():
- list(): chuyển đối tượng sang list
- map():

## Standar objects

- 'capsys': đối tượng nhận các giá trị được xuất ra màn hình
- '*args': đối tượng cho phép truyền số lượng đối số đơn lẻ chưa xác định
- '**kwargs': đối tượng cho phép truyền số lượng đối số dạng key-value chưa xác định

## Những ghi chép thú vị về python

- Các đối tượng trong python có thể được phân loại thành 2 loại là mutable và immutable. Tuy nhiên sự phân loại này thiên về khía cạnh quan niệm của người thiết kế, không phải là sự phân loại về technique.
- Khi gán một giá trị cho một biến, thực chất không phải là gán giá trị đó cho biến đó. Khi đó python sẽ tạo ra một đối tượng vùng nhớ để lưu trữ giá trị này, sau đó các biến được gán sẽ tham chiếu đến đối tượng này.
