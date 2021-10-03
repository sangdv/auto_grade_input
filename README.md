# I. Hướng dẫn cài đặt  
1. Cài đặt python3: https://www.python.org/downloads/  
2. Cài đặt các gói cần thiết 
``` 
pip3 install -r requirements.txt  
```

# II. Auto nhập điểm  
1. Chuẩn bị nội dung file csv gồm 2 cột có tiêu đề là *mssv* và *grade*. Cột *mssv* chứa danh sách các mã số sinh viên, cột *grade* chứa điểm sinh viên. Sử dụng ";" làm dấu ngăn cách các giá trị trong csv.
Ví dụ nội dung file csv như dưới đây: 
``` 
mssv;grade  
20200661;10  
20204900;4.5  
20204877;6,5  
```

2. Copy đoạn code sau vào console của python để bắt đầu quá trình nhập điểm tự động:
```
python3 auto_grade_input.py --email EMAIL_TRUONG --password MAT_KHAU --classcode MA_LOP_HOC --gradefile CSV_PATH
```
Trong đó:  
- **EMAIL_TRUONG** là email do trường cung cấp  
- **MAT_KHAU** là mật khẩu để đăng nhập vào hệ thống ctt-sis  
- **MA_LOP_HOC** là mã lớp học cần nhập điểm. Nếu nhập điểm quá trình nhớ thêm chữ "q" vào trước, chẳng hạn, "q119435". Nếu nhập điểm cuối kỳ chỉ cần nhập mã lớp học.  
- **CSV_PATH** là đường dẫn tới file csv chứa điểm và mssv đã tạo ở bước 1. Nếu file csv cùng thư mục với file auto_mark_input.py thì chỉ cần nhập tên file csv.

Ví dụ:
```
python3 auto_grade_input.py --email a.nguyenvan@hust.edu.vn --password 123456 --classcode q119435 --gradefile grade.csv
```

**Lưu ý:** Chương trình sẽ hiển thị thông tin những sinh viên có trong file csv những không tìm thấy trong ctt-sis để nhập điểm. 

3. Nhập mã captcha: có 8 giây để đọc và gõ mã captcha vào ô. Gõ xong chờ đủ 8 giây để chương trình tiếp tục chạy. Nhớ **KHÔNG** được ấn nút Đăng nhập! 

4. Mọi thứ tiếp tục được chạy tự động, không can thiệp vào cửa sổ trình duyệt trong quá trình chạy. Sau khi bot chạy xong, cần kiểm tra kỹ lại các điểm đã nhập trước khi nộp điểm cho trường. 
5. Ấn phím bất kỳ trên console chạy lệnh để thoát.