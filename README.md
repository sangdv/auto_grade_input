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

2. Copy đoạn code sau để bắt đầu nhập điểm tự động:
```
python3 auto_mark_input.py \
    --email EMAIL_TRUONG \
    --password MAT_KHAU \
    --classcode MA_LOP_HOC \ 
    --gradefile CSV_PATH
```
Trong đó:  
- EMAIL_TRUONG là email do trường cung cấp  
- MAT_KHAU là mật khẩu để đăng nhập vào hệ thống ctt-sis  
- MA_LOP_HOC là mã lớp học cần nhập điểm. Nếu nhập điểm quá trình nhớ thêm chữ "q" vào trước, chẳng hạn, "q119499". Nếu nhập điểm cuối kỳ chỉ cần nhập mã lớp học.  
- CSV_PATH là đường dẫn tới file csv chứa điểm và mssv đã tạo ở bước 1. Nếu file csv cùng thư mục với file auto_mark_input.py thì chỉ cần nhập tên file csv.  

**Lưu ý:** Chương trình sẽ hiển thị thông tin những sinh viên có trong file csv những không tìm thấy trong ctt-sis để nhập điểm. 

3. Ấn phím bất kỳ để kết thúc việc nhập điểm