# There are a lot of tips and tricks for "Pythonista"

## Optimize runtime

1. Turn off unwanted warning in python (I mostly use while plotting)

``` Python
import warnings
warnings.filterwarnings("ignore")
```

2."if __name__ == '__main__':" for discard unwanted running-code when importing a file

## Command Promt

1. python -s [filename] : run python file without module `site`

2. python --version : kiểm tra phiên bản python interpreter đang dùng

3. python -m [filename] : thực thi file theo dạng modules

## Tips

1. Với những immutable object, nên ưu tiên việc return về kết quả sau khi xử lý hàm.

2. Có thể sử dụng danh sách thay thế cho chuỗi trong xử lý chuỗi.

3. Có thể sử dụng kĩ thuật biến cờ hiệu để bỏ qua phần tử đầu tiên của một iterator.

4. Khi sử dụng mệnh đề if, nếu giá trị sử dụng là chân trị hoặc muốn biết sự tồn tại thì có thể sử dụng trực tiếp không cần phép so sánh nào.

5. Có thể tối ưu hóa việc nối chuỗi bằng cách sử dụng StringIO hoặc phương thức join.

6. Khi chỉ định giá trị cho tham số, với tham số là biến rời rạc thì dùng `None` để kiểm soát giá trị mặc định, với tham số là biến đếm thì mặc định `-1` để áp dụng cho toàn bộ.

7. Khi muốn tạo một đối tượng filter, có thể sử dụng tuple cho tối ưu.

8. Sử dụng biến cờ hiệu để skip phần tử đầu tiên.

9. Những điều kiện trả về cùng một kết quả có thể hợp nhất lại với nhau.

10. Xem xét sử dụng Generator Expression để tối ưu câu lệnh lặp hoặc sử dụng kết hợp với các hàm Aggregation.

11. Hãy sử dụng str.isspace() để check kí tự khoảng trắng

12. Hãy sử dụng buffer khi cần cắt chuỗi theo từng đoạn

13. Generator Expression nên được sử dụng khi cần tạo một pipeline mà cần duyệt qua __từng phần tử__, sau đó xử lý và trả về giá trị của phần tử đó

14. Ternary Operator nên được sử dụng khi mệnh đề if cần trả về giá trị và chức năng của từng mệnh đề if else là như nhau (cùng thực hiện một công việc)
