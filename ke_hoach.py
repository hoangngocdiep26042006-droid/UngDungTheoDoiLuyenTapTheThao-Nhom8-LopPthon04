class BaiTap:
    """Mô tả một bài tập có thể được đưa vào kế hoạch."""

    def __init__(self, ma_bai_tap, ten_bai_tap, nhom_co="Toàn thân", do_kho="Vừa"):
        if not ma_bai_tap or not ten_bai_tap:
            raise ValueError("Mã bài tập và tên bài tập không được để trống.")
        self.ma_bai_tap = str(ma_bai_tap)
        self.ten_bai_tap = ten_bai_tap.strip()
        self.nhom_co = nhom_co
        self.do_kho = do_kho

    def to_dict(self):
        return {
            "ma_bai_tap": self.ma_bai_tap,
            "ten_bai_tap": self.ten_bai_tap,
            "nhom_co": self.nhom_co,
            "do_kho": self.do_kho,
        }


class KeHoachLuyenTap:
    """Kế hoạch có danh sách bài tập và mục tiêu thời gian."""

    def __init__(self, ma_ke_hoach, ten_ke_hoach, ngay_bat_dau,
                 ngay_ket_thuc, muc_tieu_thoi_gian=0):
        if not ma_ke_hoach or not ten_ke_hoach:
            raise ValueError("Mã và tên kế hoạch không được để trống.")
        if int(muc_tieu_thoi_gian) < 0:
            raise ValueError("Mục tiêu thời gian không được âm.")
        if ngay_ket_thuc < ngay_bat_dau:
            raise ValueError("Ngày kết thúc phải bằng hoặc sau ngày bắt đầu.")
        self.ma_ke_hoach = str(ma_ke_hoach)
        self.ten_ke_hoach = ten_ke_hoach.strip()
        self.ngay_bat_dau = ngay_bat_dau
        self.ngay_ket_thuc = ngay_ket_thuc
        self.muc_tieu_thoi_gian = int(muc_tieu_thoi_gian)
        self.danh_sach_bai_tap = []

    def them_bai_tap(self, bai_tap):
        if not isinstance(bai_tap, BaiTap):
            raise TypeError("Đối tượng phải là một BaiTap.")
        self.danh_sach_bai_tap.append(bai_tap)

    def xoa_bai_tap(self, ma_bai_tap):
        for bai_tap in self.danh_sach_bai_tap:
            if bai_tap.ma_bai_tap == str(ma_bai_tap):
                self.danh_sach_bai_tap.remove(bai_tap)
                return True
        return False

    def tinh_tien_do(self, tong_thoi_gian_da_tap):
        if self.muc_tieu_thoi_gian == 0:
            return 0.0
        return round(min(tong_thoi_gian_da_tap / self.muc_tieu_thoi_gian * 100, 100), 2)

    def to_dict(self):
        return {
            "ma_ke_hoach": self.ma_ke_hoach,
            "ten_ke_hoach": self.ten_ke_hoach,
            "ngay_bat_dau": self.ngay_bat_dau,
            "ngay_ket_thuc": self.ngay_ket_thuc,
            "muc_tieu_thoi_gian": self.muc_tieu_thoi_gian,
            "danh_sach_bai_tap": [b.to_dict() for b in self.danh_sach_bai_tap],
        }
