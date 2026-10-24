# Phân công class cho 4 thành viên
   
# Thành viên 1 — Hồ sơ và mục tiêu
File: ho_so.py, muc_tieu.py
HoSoNguoiDung: lưu thông tin người dùng, chiều cao, cân nặng.
MucTieu: tạo mục tiêu tập luyện và tính tỷ lệ hoàn thành.
ChiSoCoThe: ghi nhận các chỉ số cơ thể theo ngày.
Phụ trách: Thuộc tính, phương thức, đóng gói và kiểm tra dữ liệu đầu vào.


# Thành viên 2 — Môn tập và buổi tập
File: mon_tap.py, buoi_tap.py
MonTap: thông tin môn thể thao.
BuoiTap: lưu kết quả buổi tập.
BuoiTapChayBo: kế thừa BuoiTap.
BuoiTapDapXe: kế thừa BuoiTap.
BuoiTapGym: kế thừa BuoiTap.
PhuongPhapTinhDiem: lớp trừu tượng để quy định cách tính điểm.
Phụ trách: Kế thừa, đa hình, trừu tượng và phương thức tính điểm theo môn.


# Thành viên 3 — Kế hoạch và thống kê
File: ke_hoach.py, thong_ke.py, nhac_lich.py
BaiTap: mô tả bài tập cụ thể.
KeHoachLuyenTap: tạo và quản lý kế hoạch.
ThongKeLuyenTap: tính tổng thời gian, số buổi và tiến độ.
NhacLich: quản lý lịch tập dự kiến.
Phụ trách: Xử lý nghiệp vụ, tính toán và phối hợp các đối tượng.


# Thành viên 4 — Quản lý dữ liệu và tích hợp
File: du_lieu.py, quan_ly.py, main.py
QuanLyDuLieu: đọc và ghi JSON/CSV.
QuanLyLuyenTap: điều phối thêm, sửa, xóa, tìm kiếm và lọc buổi tập.
main.py: tạo đối tượng và chạy thử chương trình.
Phụ trách: Import class của các thành viên, kết nối chức năng, kiểm thử và sửa lỗi tích hợp.
