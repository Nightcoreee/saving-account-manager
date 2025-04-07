# 💰 ỨNG DỤNG QUẢN LÝ SỔ TIẾT KIỆM
## 📌 Giới thiệu thành viên - Nhóm 09
|Tên thành viên | Mã số sinh viên |
|---------------|-----------------|
|Đào Ngọc Hà    | 3121411062 |
|Trần Hửu Hậu   | 3121411068 |
|Võ Khánh Linh  | 3121411122 |
|Nguyễn Ngọc Khôi | 3121411108|
## 📌 Giới Thiệu
Ứng dụng quản lý sổ tiết kiệm giúp người dùng theo dõi và quản lý các khoản tiết kiệm cá nhân một cách dễ dàng.  
Với giao diện trực quan, người dùng có thể:
- Mở sổ tiết kiệm
- Gửi tiền vào sổ
- Rút tiền khỏi sổ
- Tính lãi suất
- Đóng sổ tiết kiệm

Ứng dụng phù hợp với cá nhân muốn theo dõi tình hình tiết kiệm của mình một cách chi tiết và hiệu quả. 🚀  

---

## 🌟 Tính Năng Chính
✅ **Mở sổ tiết kiệm**: Tạo sổ tiết kiệm với thông tin về kỳ hạn, lãi suất và số tiền gửi ban đầu.  
✅ **Gửi tiền vào sổ**: Cho phép nạp thêm tiền vào tài khoản tiết kiệm theo quy định.  
✅ **Rút tiền khỏi sổ**: Hỗ trợ rút một phần hoặc toàn bộ số tiền gửi.  
✅ **Tính lãi suất**: Tự động tính lãi suất dựa trên kỳ hạn và số dư tài khoản.  
✅ **Đóng sổ tiết kiệm**: Kết thúc sổ tiết kiệm và hiển thị số tiền cuối cùng.  

---

## 🛠 Công Nghệ Sử Dụng
- **Ngôn ngữ**: Python  
- **Giao diện**: Tkinter  
- **Cơ sở dữ liệu**: MySQL  
- **Thư viện hỗ trợ**: Pandas, openpyxl (xuất Excel), datetime  

---

## 📅 Kế Hoạch Phát Triển (Development Plan)

| Giai đoạn       | Công việc                             | Thời gian hoàn thành|
|-----------------|----------------------------------------------------|--------|
| **Giai đoạn 1** | Phân tích yêu cầu, xác định phạm vi dự án          | 1 tuần |
| **Giai đoạn 2** | Thiết kế giao diện ứng dụng với Tkinter            | 1 tuần |
| **Giai đoạn 3** | Xây dựng hệ thống lưu trữ với MySQL                | 1 tuần |
| **Giai đoạn 4** | Phát triển chức năng chính (mở, gửi, rút, đóng sổ) | 1 tuần |
| **Giai đoạn 5** | Kiểm thử ứng dụng, sửa lỗi                         | 1 tuần |
| **Giai đoạn 6** | Hoàn thiện tài liệu hướng dẫn sử dụng              | 1 tuần |
| **Giai đoạn 7** | Triển khai bản chính thức                          | 1 tuần |

⏳ **Tổng thời gian dự kiến**: 6-7 tuần  

## Sơ đồ Use Case 
![image](https://github.com/user-attachments/assets/694fa503-6dce-4ab6-aa6a-a0a071731943)

## Sơ đồ Class Diagram
![image](https://github.com/user-attachments/assets/c2951d2e-959e-4597-a664-065d5d6f112a)
# Mô tả chi tiết sơ đồ
System:
Đây là lớp đại diện cho toàn bộ hệ thống ngân hàng.
Thuộc tính:
calculateInterest(): Có thể là một phương thức để tính toán lãi suất cho các tài khoản.
generateStatement(): Có thể là một phương thức để tạo báo cáo giao dịch.
User:
Đại diện cho người dùng (khách hàng) của hệ thống ngân hàng.
Thuộc tính:
User ID: Mã định danh duy nhất của người dùng.
Name: Tên của người dùng.
Email: Địa chỉ email của người dùng.
Gender: Giới tính của người dùng.
Address: Địa chỉ của người dùng.
Phone: Số điện thoại của người dùng.
AC Open: Ngày mở tài khoản (có vẻ không phù hợp ở lớp User, có thể nên ở lớp Saving Account).
Phương thức:
Open Account(): Mở một tài khoản mới.
Deposit(): Gửi tiền vào tài khoản.
Withdraw(): Rút tiền khỏi tài khoản.
View Transaction History(): Xem lịch sử giao dịch của tài khoản.
Employee:
Đại diện cho nhân viên của ngân hàng.
Thuộc tính:
Employ ID: Mã định danh duy nhất của nhân viên.
Name: Tên của nhân viên.
Gender: Giới tính của nhân viên.
Email: Địa chỉ email của nhân viên.
Password: Mật khẩu đăng nhập của nhân viên.
Phương thức:
VerifyTransaction(): Xác minh một giao dịch.
Login(): Đăng nhập vào hệ thống.
Saving Account:
Đại diện cho tài khoản tiết kiệm của người dùng.
Thuộc tính:
Account ID: Mã định danh duy nhất của tài khoản.
User ID: Mã định danh của người sở hữu tài khoản (khóa ngoại liên kết với lớp User).
Account Number: Số tài khoản ngân hàng.
Date: Ngày tạo tài khoản.
Balance: Số dư hiện tại trong tài khoản.
InterestRate: Lãi suất hiện tại của tài khoản.
CreateDate: Ngày tạo tài khoản (có vẻ trùng lặp với Date).
Status: Trạng thái của tài khoản (ví dụ: active, inactive).
Phương thức:
CalculateInterest(): Tính toán lãi suất cho tài khoản này.
AddTransaction(): Thêm một giao dịch vào lịch sử của tài khoản.
Transaction:
Đại diện cho một giao dịch được thực hiện trên tài khoản.
Thuộc tính:
Transaction ID: Mã định danh duy nhất của giao dịch.
Account ID: Mã định danh của tài khoản liên quan đến giao dịch (khóa ngoại liên kết với lớp Saving Account).
Date: Ngày và giờ thực hiện giao dịch.
Amount: Số tiền giao dịch.
Type: Loại giao dịch (ví dụ: deposit, withdrawal).
Phương thức:
generateReceipt(): Tạo một biên lai cho giao dịch này.
Receipt:
Đại diện cho một biên lai giao dịch.
Thuộc tính:
Receipt ID: Mã định danh duy nhất của biên lai.
Transaction ID: Mã định danh của giao dịch mà biên lai này liên quan đến (khóa ngoại liên kết với lớp Transaction).
Content: Nội dung chi tiết của biên lai.
IssuedDate: Ngày phát hành biên lai.
Phương thức:
print(): In biên lai.
InterestRateTerm:
Đại diện cho các kỳ hạn và lãi suất khác nhau mà ngân hàng cung cấp.
Thuộc tính:
Term ID: Mã định danh duy nhất của kỳ hạn.
Term (D): Thời gian kỳ hạn (có thể là số ngày).
Interest Rate: Mức lãi suất tương ứng với kỳ hạn.
Effective Date: Ngày mà mức lãi suất này có hiệu lực.
Phương thức:
isValid(): Kiểm tra xem kỳ hạn và lãi suất này có còn hiệu lực hay không.
Notification:
Đại diện cho các thông báo được gửi đến người dùng.
Thuộc tính:
Noti ID: Mã định danh duy nhất của thông báo.
To Email: Địa chỉ email người nhận thông báo.
Date: Ngày gửi thông báo.
Message: Nội dung của thông báo.
sendDate: Ngày gửi thông báo (có vẻ trùng lặp với Date).
Phương thức:
Send Email(): Gửi thông báo qua email.

