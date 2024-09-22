Một số câu lệnh được dùng trong linux terminal:
* cd: di chuyển trong cây thư mục
* echo: show một hoặc nhiều chuỗi văn bản (biến string cũng có thể xem là một văn bản)
* ls: kiệt kê tài nguyên trong thư mục
* touch: tạo mới một file, nếu tồn tại thì cập nhật trạng thái
* rm: xóa bỏ một file
* which (unix only): tìm đường dẫn tới một file thực thi trong PATH
    + '-a': xuất tất cả đường dẫn có file thực thi
* mkdir: tạo mới một hoặc nhiều thư mục
* chmod: thay đổi quyền truy cập của file hay folder
* export: tạo hoặc thay đổi giá trị một biến môi trường. LƯU Ý: biến môi trường được tạo bằng 'export' chỉ có hiệu lực trong cửa sổ hoặc phiên làm việc hiện tại, và các biến này sẽ được chuyển giao cho các tiến trình con.
* pwd: xuất ra địa chỉ thư mục hiện
* rm: xóa một hoặc nhiều thư mục  

Một số biến môi trường thông dụng trong linux:
* PATH: lưu đường dẫn những folder chứa file thực thi
* PWD: lưu địa chỉ của thư mục hiện hành

Các toán tử và kí hiệu được dùng trong terminal:
* '$' hoặc '#' ở đầu dòng: ký tự nhắc dòng lệnh, tùy thuộc vào quyền hạn của người đang dùng.
* '>': toán tử chuyển hướng, ghi kết quả đầu ra vào một file.
* '!$': biến được sử dụng để tham chiếu đến đối số cuối cùng của câu lệnh trước đó.
* '$?': biến chứa mã thoát (exit hoặc return value) của câu lệnh trước đó


Tài nguyên trong môi trường ảo (venv) sẽ được ưu tiên hơn những tài nguyên thông thường.

Các quyền truy cập trong linux:
* Quyền đọc (read)(r)
* Quyền ghi (write)(w)
* Quyền thực thi (execute)(x)

Tips & Tricks:
- Cố gắng sử dụng các biến môi trường để rút ngắn địa chỉ nhất có thể.
