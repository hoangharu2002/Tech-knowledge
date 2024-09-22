# Tổng hợp nội dung về hệ thống cơ sở dữ liệu

Có 3 mức để biểu diễn một hệ thống cơ sở dữ liệu:

- Mức ngoài (View)
- Mức quan niệm (trừu tượng)
- Mức trong (vật lý)

Xét về ngôn ngữ truy vấn, cơ sở dữ liệu có 2 loại: SQL và NoSQL

## Mức quan niệm

- Là mức biểu diễn về cấu trúc tổng thể của cơ sở dữ liệu một cách trừu tượng
- Được biểu diễn bằng các mô hình dữ liệu
- Một số mô hình dữ liệu:
  - Mô hình dữ liệu mạng (Network Data Model):
    - Còn gọi là mô hình lưới, được biểu diễn bởi một đồ thị có hướng
    - Gồm các thành phần: mẫu tin (bản ghi), loại mẫu tin, loại liên hệ, bản số (hệ số)
    - Biểu diễn theo cơ chế chủ-thành viên, chủ sẽ tạo liên kết có hướng đến thành viên để hiện mối quan hệ.
    - Ưu điểm:
      - Đơn giản, dễ sử dụng
    - Nhược điểm:
      - Khả năng diễn đạt ngữ nghĩa kém (gây khó hiểu)
      - Không thích hợp cho những CSDL quy mô lớn
  - Mô hình dữ liệu phân cấp (Hierachical Data Model):
    - Gọi tắt là mô hình phân cấp
    - Biểu diễn phân cấp dữ liệu theo dạng cây
    - Giữa nút con với nút cha được liên kết theo một mối quan hệ nhất định
    - Gồm các thành phần: loại mẫu tin, loại mối liên hệ
    - Giữa hai loại mẫu tin chỉ tồn tại một mối quan hệ duy nhất: từ chủ tới thành viên (1-n), từ thành viên tới chủ (1-1)
    - Ưu điểm:
      - Đơn giản, dễ sử dụng, tìm kiếm nhanh
    - Nhược điểm:
      - Diễn đạt ngữ nghía kém (khó áp dụng cho những quan hệ phức tạp)
      - Không thích hợp cho những CSDL quy mô lớn
  - Mô hình dữ liệu thực thể mối kết hợp (ER Model - Entity Relationship Model):
    - Còn được gọi là mô hình thực thể mối liên kết
    - Biểu diễn bằng việc trừu tượng hóa các đối tượng trong thế giới thực thành các thực thể cùng mối liên kết giữa chúng thành dạng biểu đồ
    - Gồm các thành phần: thực thể, loại thực thể, thuộc tính [optional], mối liên kết (mối kết hợp)
    - Thuộc tính trong ER Model được chia thành các loại:
      - Đơn trị (simple): thuộc tính chỉ chứa một giá trị, ứng với mỗi đối tượng
      - Đa trị (multi-valued): thuộc tính có thể có nhiều giá trị
      - Đa hợp (composite): thuộc tính có thể được tạo từ nhiều thành phần
    - Các đặc điểm của thuộc tính:
      - Thuộc tính đa hợp và đa trị có thể lòng nhau tùy ý
      - Thuộc tính có thể suy diễn (thuộc tính dẫn xuất): thuộc tính có thể có được bằng cách tính toán từ các thuộc tính có sẵn khác
      - Trong trường hợp không thể xác định được giá trị, sử dụng giá trụ null
      - Mỗi loại thực thể sẽ có một hoặc một nhóm các thuộc tính được dùng để nhận diện các thực thể, gọi là khóa chính
    - Một số lưu ý:
      - Mỗi loại thực thể phải có 1 khóa chính
      - Một khóa có thể có nhiều thuộc tính
      - Có thể có nhiều khóa trong một loại thực thể, cần chọn 1 để làm khóa chính
      - Số ngôi của một mối kết hợp là số loại thực thể tham gia vào mối kết hợp đó
    - Ưu điểm:
      - Mô tả được thế giới thực, gần gũi với con người
      - Thích hợp cho những hệ thống CSDL từ nhỏ đến lớn
    - Nhược điểm:
      - Đòi hỏi tư duy xây dựng CSDL tốt
      - Cần thời gian phân tích và thiết kế để đạt được sự hiệu quả
  - Mô hình dữ liệu quan hệ (Relational Data Model):
    - Gồm các thành phần:
      - Thuộc tính (Attribute): mô tả đặc trưng của đối tượng. Ký hiệu miền giá trị của thuộc tính `Dom(Attribute)={Domain}`
      - Quan hệ (Relation): là tập hữu hạn các thuộc tính. Ký hiệu: `R(A1, A2, A3,...)`, quan hệ R và các thuộc tính (A1, A2, A3,...)
      - Bộ giá trị (Tuple): là các thông tin của một đối tượng thuộc quan hệ. Ký hiệu: `t=(a1, a2, a3,...)`, đối tượng t có bộ giá trị (a1, a2, a3,...)
      - Quan hệ là một bảng, các cột là các thuộc tính, các dòng là các bộ giá trị.
      - Thể hiện của quan hệ tại một thời điểm (Instance), ký hiệu T.
      - Tân từ: là một quy tắc dùng để mô tả một quan hệ, làm rõ ngữ nghĩa và sự liên hệ giữa các thuộc tính trong quan hệ. Ký hiệu: ||R||.
      - Phép chiếu quan hệ lên tập thuộc tính, ký hiệu: R[X] hoặc R.X (nếu X có 1 thuộc tính), có thể hiểu đơn giản phép chiếu là trích xuất giá trị của một tập hợp các thuộc tính nào đó của quan hệ.
      - Phép chiếu một bộ lên tập thuộc tính, ký hiệu: tR[X] hoặc t[X] hoặc tR.X (nếu X có 1 thuộc tính)
      - Các loại khóa trong mô hình dữ liệu quan hệ:
        - Siêu khóa (super key):
          - Một quan hệ có thể có nhiều siêu khóa
          - Một siêu khóa có thể có nhiều thuộc tính
        - Khóa (key)
          - Khóa là siêu khóa có kích thước nhỏ nhất
          - Một quan hệ có thể có nhiều khóa
          - Các thuộc tính tham giao vào khóa được gọi thuộc tính khóa
        - Khóa chính (primary key)
          - Là một khóa được chọn để trở thành khóa chính
          - Một quan hệ chỉ có 1 khóa chính
          - Khóa chính không được chứa giá trị null
        - Khóa ngoại (foreign key)
          - Khóa ngoại của một quan hệ sẽ tham chiếu đến khóa chính của một quan hệ khác, hay nói cách khác là dùng khóa chính của một quan hệ khác để làm khóa ngoại cho quan hệ này
          - Việc tạo khóa ngoại sẽ làm tăng tính liên kết giữa các quan hệ trong cơ sở dữ liệu
          - Một thuộc tính có thể vừa tham gia vào khóa chính, vừa tham gia vào khóa ngoại
          - Khóa ngoại có thể tham chiếu đến khóa chính trên cùng 1 lược đồ quan hệ
          
        - Khóa tương đương: là các khóa còn lại nhưng không được chọn làm khóa chính
  - Mô hình dữ liệu hướng đối tượng