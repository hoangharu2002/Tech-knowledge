# General

Python hiện đang là một trong những ngôn ngữ lập trình phổ biến bậc nhất trên thế giới, được ứng dụng trong nhiều lĩnh vực.

Python có hai phiên bản gồm Python2 và Python3:

- Python2: đã cũ và có lẽ không còn được hỗ trợ, so với Python3 thì thiếu đi một số tính năng. Tuy nhiên vẫn còn được sử dụng phần lớn trong nhiều hệ thống cũ.
- Python3: là phiên bản hiện đại hơn và đang được sử dụng.

Môi trường ảo trong Python có chức năng giống như Sandbox, lập trình viên có thể cài đặt và làm việc tùy ý trong môi trường ảo mà không ảnh hưởng đến môi trường hệ thống. Hai công cụ tạo môi trường ảo phổ biến là 'venv' và 'virtualenv'. 'venv' tạo môi trường ảo với các tính năng cơ bản, đơn giản và được cài đặt sẵn cùng với python. 'virtualenv' là một công cụ của bên thứ ba nên cần được cài đặt thông qua 'pip', có nhiều tính năng hơn và khả năng tương thích tốt hơn với nhiều phiên bản python.

Một số problem khi lập trình với Python:

- Sử dụng trick "if __name__ == '__main__':" để kiểm soát việc chạy code dưới dạng Script và Module.
- Chạy file không có module 'site': "python -s [filename]"
- Chạy file script dưới dạng module: "python -m [filename]"
- Tạo môi trường ảo: "python -m venv|virtualenv [virtual_folder_name]"
- Hàm thoát 'exit()' trong python thường được thêm tự động bởi module 'site', trường hợp không dùng module 'site' hệ thống sẽ báo lỗi, sửa lỗi bằng cách "sys.exit()" hoặc "raise SystemExit()"
- Sử dụng @decorator để thay đổi hoặc mở rộng một hàm đã có mà không cần phải thay đổi code của nó. Một số decorator: @property, @classmethod, @staticmethod...
- Những thực thi mang tính hệ thống nên được xử lý bên trong hàm main(), không nên được xử lý bên trong các hàm cục bộ.

## Một số thư viện hỗ trợ của Python

- 'Six'(?): thư viện hỗ trợ viết mã tương thích cho Python2 và Python3.
- 'sys': thư viện liên kết với hệ thống.
- 'argparse'(*): thư viện mạnh mẽ để xử lý các đối số dòng lệnh (command line).
- 'pytest'(*): công cụ kiểm thử, thư viện hỗ trợ viết unit tests và kiểm soát exception.
- 'mypy': công cụ kiểm tra các lỗi liên quan đến khai báo và sử dụng kiểu dữ liệu, thư viện cung cấp khả năng tạo các nhãn kiểu dữ liệu một cách linh hoạt.
- 'site': module mặc định khi làm việc với python, được thêm vào tự động mỗi khi thực thi trong môi trường python bình thường, có chức năng thêm vào các cấu hình ban đầu cũng như thêm vào các hàm, thư viện... và set up đường dẫn tới các thư viện của hệ thống.
- 'functools': module được tích hợp sẵn trong python, cung cấp các công cụ tiện ích cho việc xử lý và thao thác với các hàm.
- 'pprint': module hỗ trợ việc in các cấu trúc dữ liệu phức tạp được gọn gàng và đẹp hơn.
** Chú thích: Dấu (*) thể hiện package được hỗ trợ bởi bên thứ ba. Dấu (?) thể hiện những package chưa được thử nghiệm.

## Một số tool hỗ trợ

- [pip](..\frameworks\pip.md): trình quản lý gói cho python, hỗ trợ cài đặt các gói từ PyPI (Python Package Index - một kho lưu trữ trực tuyến các gói phần mềm Python)

## Một số hàm trong python

- dir(): liệt kê các thành phần (thuộc tính, phương thức,...) của một module hoặc một đối tượng.
- sorted(): sắp xếp lại các giá trị trong một đối tượng.

## Một số đối tượng quan trọng trong python

- 'capsys': đối tượng nhận các giá trị được xuất ra màn hình
- '*args': đối tượng cho phép truyền số lượng đối số đơn lẻ chưa xác định
- '**kwargs': đối tượng cho phép truyền số lượng đối số dạng key-value chưa xác định
