Hệ thống file phân tán (DFS - Distributed File System) là một hệ thống quản lý file được phân tán thành các file servers hoặc nhiều địa điểm khác nhau.

Mục đích chính của DFS đó là cho phép người dùng của những hệ thống phân tán vật lý có thể chia sẻ dữ liệu cũng như tài nguyên bằng cách sử dụng Hệ thống file chuyên dụng (CFS - Common File System).

Một DFS được thực thi như một phần của hệ điều hành.

DFS có hai thành phần:
* Location Transparency (namespace component - sự minh bạch)
* Redundancy (replication component - sự rườm rà)

=> Trong trường hợp failure và heavy load, những thành phần này sẽ đảm bảo tính có sẵn của dữ liệu bằng cách cho phép chia sẻ dữ liệu ở những địa điểm khác nhau được nhóm lại một cách logic dưới dạng một thư mục, được biết đến đó là "DFS root".

=> Không nhất thiết phải sử dụng cả hai thành phần của DFS cùng nhau. Có thể sử dụng namespace mà không cần sử dụng replication, và cũng hoàn toàn có thể sử dụng replication mà không dùng namespace giữa các servers.

File system replication:

* Những bản sao đầu tiên của DFS tận dụng Microsoft's File Replication Service, cho phép tịnh tiến file replication giữa các servers. Phần lớn những bản sao gần đây của cả file được phân tán đến tất cả servers bằng FRS, thứ sẽ nhận diện file mới hoặc đã cập nhật.

* Sau này FRS được thay thế bởi "DFS Replication", được phát triển bởi Windows Server 2003 R2 (DFSR). Bằng cách copy những phần của những file mà có sự thay đổi và giảm lưu lượng mạng với việc nén dữ liệu, nó giúp làm cải thiện FRS. Thêm vào đó, nó cung cấp cho người dùng những tùy chọn cấu hình linh hoạt để quản lý lưu lượng mạng trên một lịch trình cấu hình => DFSR ưu điểm hơn FRS ở điểm cho phép người dùng cấu hình lưu lượng mạng.

# Các đặc điểm của DFS:
* Transparency (tính minh bạch): cho phép người dùng thao tác với file trong hệ thống như file ở local.
* User mobility (tính di động của người dùng): người dùng có thể truy cập hệ thống bằng nhiều loại thiết bị hay từ nhiều vị trí khác nhau.
* Performance (hiệu suất): những yếu tố ảnh hưởng đến hiệu suất của hệ thống gồm:
    - Thông lượng: mức độ dữ liệu có thể được truyền giữa các node. Thông lượng cao đảm bảo lượng lớn dữ liệu có thể được xử lý và truyền một cách hiệu quả, giảm thiểu độ trễ và cải thiện hiệu suất hệ thống.
    - Độ trễ: là sự trì trệ phát sinh trong quá trình truy cập dữ liệu trong hệ thống file phân tán. Giảm độ trễ chủ yếu để cải thiện thời gian phản hồi và đảm bảo trải nghiệm người mượt mà.
    - Khả năng mở rộng: một hệ thống file phân tán có khả năng mở rộng khi kiểm soát được lượng dữ liệu và yêu cầu người dùng gia tăng mà không làm giảm hiệu suất của cả hệ thống.
    - Tính đồng thời: khả năng hỗ trợ nhiều người dùng và ứng dụng truy cập dữ liệu cùng một lúc.
    - Khả năng chịu lỗi: đảm bảo hệ thống vẫn hoạt động và truy cập được khi xảy ra sự cố.
    - Dữ liệu địa phương (Data Locality): ưu tiên lưu trữ và truy cập dữ liệu ở khu vực gần với nhu cầu.
    - Quản lý Metadata: quản lý metadata cũng góp phần duy trì hiệu suất hệ thống, đặc biệt là trong môi trường phân tán quy mô lớn.
    - Sử dụng băng thông mạng (Network Bandwidth Utilization): tối ưu hóa sử dụng mạng, đảm bảo truyền dữ liệu hiệu quả và giảm "nút cổ chai" trong hệ thống.
* Simplicity and ease of use (đơn giản và dễ sử dụng): hệ thống sẽ cung cấp giao diện trực quan, những tính năng và cơ chế để hỗ trợ, hạn chế sự can thiệp thủ công của người dùng nhất có thể.
* High availability (tính sẵn có cao): một đặc tính quan trọng của các hệ thống phân tán, nhằm đảm bảo tính sẵn có, truy cập được và hoạt động được bất cứ khi nào cần.
* Scalability (khả năng mở rộng): hệ thống có khả năng kiểm soát sự gia tăng về lượng dữ liệu, người dùng cũng như tải hệ thống trong khi vẫn duy trì được hiệu suất, độ tin cậy và khả năng quản lý mà không cần những thay đổi phức tạp hay làm giảm hiệu quả.
* High reliability (độ tin cậy cao): khả năng xảy ra mất dữ liệu nên được giảm thiểu hết mức có thể trong một hệ thống file phân tán thích hợp. Đó là, vì sự không đáng tin cậy của hệ thống, người dùng không nên cảm thấy ép buộc khi phải tạo backup cho file của họ. Hơn hết, một hệ thống file nên tạo backup của những file quan trọng mà có thể được sử dụng nếu file gốc bị mất. Nhiều hệ thống file sử dụng lưu trữ ổn định như một chiến lược tin cậy cao.
* Data integrity (tính toàn vẹn dữ liệu): nhiều người dùng thường xuyên chia sẻ hệ thống file. Tính toàn vẹn của dữ liệu được lưu trong một file được chia sẻ phải được đảm bởi hệ thống file. Đó là, những yêu cầu truy cập đồng thời từ nhiều người dùng, những người đang cạnh tranh cho việc truy cập vào cùng một file phải được đồng bộ hóa chính xác khi sử dụng một phương pháp điều khiển đồng thời. Atomic transaction là một cơ chế quản lý đồng thời cấp cao thường được hệ thống file cung cấp cho người dùng.
* Security (bảo mật): một hệ thống file phân tán nên được bảo mật để những người dùng có thể tin tưởng rằng dữ liệu của họ sẽ được giữ riêng tư. Để bảo vệ thông tin được chứa bên trong hệ thống file từ những truy cập không mong muốn và chưa xác định, các cơ chế bảo mật phải được thực thi.
* Heterogeneity (tính không đồng nhất): tính không đồng nhất trong hệ thống phân tán là không thể tránh khỏi như một hệ quả của quy mô rộng lớn. Người dùng của những hệ thống phân tán không đồng nhất có lựa chọn trong việc sử dụng nhiều nền tảng máy tính cho nhiều mục đích khác nhau.

# Các kĩ thuật và thuật toán được sử dụng trong DFS:
- Load balancing
- Distributed locking
- Versioning
- Synchronization protocols
- Data replication
- Data caching
- Data routing
- Transaction management
- Data partitioning
- Redundancy
- Error recovery
- Intelligent data placement
- Metadata caching
- Indexing
- Hierarchical namespace organization
- Data compression
- Data deduplication
- Adaptive data transfer 
- Automatic error detection
- Automatic failover

# Giải thích tại sao các file copy và địa chỉ của chúng được "che giấu" giữa các nodes:
- Load Balancing (cân bằng tải): việc che giấu vị trí của những file copy khiến DFS phân tán các requests đồng đều trên nhiều nodes, nơi lưu trữ những file copy. Điều này giúp làm cân bằng tải trên những nodes khác nhau, tránh việc bất kì một node nào trở thành nút cổ chai.

- Fault Tolerance (khả năng chịu lỗi): nếu một node chứa file copy bị lỗi, DFS có thể minh bạch chuyển hướng những requests đến những nodes khác có copy của file. Bằng cách giấu vị trí của file copy, DFS đảm bảo rằng clients sẽ không biết về việc cơ sở hạ tầng vật lý hoặc các nút riêng lẻ bị lỗi.

- Data Consistency (nhất quán dữ liệu): khi một file được cập nhật hoặc thay đổi, DFS cần đảm bảo rằng tất cả các bản sao của file được đồng bộ để duy trì sự nhất quán dữ liệu. Bằng cách trừu tượng hóa vị trí của những bản sao, DFS có thể kiểm soát được dữ liệu sao chép và sự đồng bộ hóa minh bạch, đảm bảo rằng tất cả các bản sao được cập nhật một cách nhất quán.

- Security (bảo mật): việc che giấu vị trí của các file copy cũng có thể nâng cao tính bảo mật bằng cách phòng tránh truy cập chưa xác thực đến các node cụ thể trong đó những bản sao của những file nhạy cảm được lưu trữ. Clients truy cập vào những file thông qua DFS không cần biết về vị trí vật lý của những file copy, giảm thiểu rủi ro của truy cập chưa xác thực hay mạo danh.

# Quy trình của Load Balancing trong DFS:

1.Request Distribution (yêu cầu phân tán): khi một client yêu cầu truy cập vào một file, DFS xác định node hoặc những node nào lưu trữ những bản sao của file đó. DFS sau đó phân tán yêu cầu giữa những node đó, mục đích để phân tán đồng đều khối lượng công việc.

2. Node Selection (lựa chọn node): DFS sẽ sử dụng đa dạng các thuật toán để lựa chọn những node phù hợp để thực hiện yêu cầu. Những thuật toán này có thể được dựa vào các nhân tố như là tải của node hiện tại, độ trễ của mạng, hoặc thậm chí là tiếp cận round-robin trong đó những yêu cầu được phân phối tuần tự giữa các node có sẵn.

3. Dynamic Adjustment (điều chỉnh động): các thuật toán cân bằng tải trong DFS có thể động (dynamic), nghĩa là chúng sẽ tiếp tục giám sát khối lượng công việc trên các node khác nhau và điều chỉnh phân phối của các yêu cầu cho phù hợp.

4. Fault Tolerance: cân bằng tải trogn DFS cũng phân phối đến khả năng chịu lỗi. Nếu một node bị lỗi hoặc trở nên không sẵn có, DFS có thể chuyển hướng những yêu cầu đến những node khác có lưu trữ các bản sao của cùng một file, đảm bảo rằng việc truy cập file của client không bị gián đoạn.

5. Scalability (khả năng mở rộng): cân bằng tải cho phép DFS mở rộng theo chiều ngang bằng cách thêm nhiều node hơn vào hệ thống. Vì số lượng các node tăng, DFS có thể phân tán khối lượng công việc đồng đều hơn trên lượng tài nguyên đã mở rộng, đáp ứng nhu cầu ngày càng tăng mà không làm giảm hiệu suất.
