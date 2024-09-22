# Trong SQL Server

## Ngôn ngữ tương tác cơ sở dữ liệu gồm các loại

- Data Definition Language (ngôn ngữ định nghĩa dữ liệu): được dùng để định nghĩa cấu trúc cơ sở dữ liệu, cấu trúc bảng, các điều kiện và ràng buộc.
- Data Manipulation Language (ngôn ngữ thao tác dữ liệu): được dùng để thêm, cập nhật, xóa các điểm dữ liệu trong bảng.
- Structured Query Language (ngôn ngữ truy vấn có cấu trúc): được dùng để truy vấn dữ liệu trong các bảng trong cơ sở dữ liệu

### Các kiểu dữ liệu trong SQL

- string: CHAR(n), VARCHAR(n), NCHAR(n), NVARCHAR(n), TEXT, NTEXT
- boolean: TRUE, FALSE
- date: DATETIME, SMALLDATETIME
- numeric: INT, FLOAT, NUMERIC(i, j)
    - int:
        - bigint

### Data Definition Language

** Lưu ý: các cột được định mặc định là chứa giá trị NULL

`CREATE DATABASE <csdl>` : tạo cơ sở dữ liệu  
`USE <csdl>` : sử dụng cơ sở dữ liệu  
`DROP DATABASE <csdl>` : xóa cơ sở dữ liệu

```SQL
<!-- tạo bảng trong SQL --> //////////////////////////////////////////////////////////////////////////
CREATE TABLE <table>(
    <col_1> <col_type_1>,
    <col_2> <col_type_2>,
    ...
);

<!-- xóa bảng trong SQL --> //////////////////////////////////////////////////////////////////////////
DROP TABLE <table>;

<!-- xóa một ràng buộc --> ///////////////////////////////////////////////////////////////////////////
ALTER TABLE <table>
DROP CONSTRAINT <name>;

<!-- tạo khóa chính ngoài bảng --> //////////////////////////////////////////////////////////////////
ALTER TABLE <table> ADD
CONSTRAINT <name> PRIMARY KEY (<col_name>);
    <!-- ưu điểm: linh hoạt hơn, tính tùy biến cao hơn, giảm độ phức tạp khi định nghĩa bảng>
    <!-- nhược điểm: biết về cú pháp ALTER>

<!-- tạo khóa chính trong bảng --> //////////////////////////////////////////////////////////////////


    <!-- cách 1: tạo khóa sau khi khai báo cột> ////////////////////////////////////////////
CREATE TABLE <table>(
    <col> <col_type> NOT NULL PRIMARY KEY,
    ...
);
    <!-- ưu điểm: nhanh, tiện lợi trong lúc khai báo bảng>
    <!-- nhược điểm: chỉ tạo được khóa gồm 1 cột, không tùy chỉnh được tên khóa chính>


    <!-- cách 2: tạo khóa ở cuối bảng, sau khi khai báo tất cả các cột> ////////////////////
CREATE TABLE <table>(
    <col_1> <col_type_1> NOT NULL,
    <col_2> <col_type_2>,
    ...
    CONSTRAINT <name> PRIMARY KEY (<col_name>)
);
    <!-- ưu điểm: linh hoạt hơn, khắc phục được những vấn đề của cách 1>
    <!-- nhược điểm: cần hoàn thành khai báo bảng, code nhiều hơn một chút>

<!-- tạo khóa ngoại trong bảng --> //////////////////////////////////////////////////////////////////


    <!-- cách 1: tạo khóa sau khi khai báo cột -->
CREATE TABLE <table>(
    <col> <col_type>
);

```
