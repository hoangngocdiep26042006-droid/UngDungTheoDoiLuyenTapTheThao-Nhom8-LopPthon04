from buoi_tap import BuoiTap
from thong_ke import ThongKeLuyenTap
from du_lieu import QuanLyDuLieu


class QuanLyLuyenTap:
    """Điều phối các thao tác với buổi tập, kế hoạch và dữ liệu."""

    def __init__(self, quan_ly_du_lieu=None, ten_file="buoi_tap.json"):
        self.quan_ly_du_lieu = quan_ly_du_lieu or QuanLyDuLieu()
        self.ten_file = ten_file
        self.danh_sach_buoi_tap = self.quan_ly_du_lieu.doc_danh_sach_buoi_tap(ten_file)
        self.thong_ke = ThongKeLuyenTap(self.danh_sach_buoi_tap)

    def them_buoi_tap(self, buoi_tap):
        if not isinstance(buoi_tap, BuoiTap):
            raise TypeError("Buổi tập phải là đối tượng BuoiTap hoặc lớp con.")
        if any(b.ma_buoi_tap == buoi_tap.ma_buoi_tap for b in self.danh_sach_buoi_tap):
            raise ValueError(f"Mã buổi tập {buoi_tap.ma_buoi_tap} đã tồn tại.")
        self.danh_sach_buoi_tap.append(buoi_tap)
        self._dong_bo()

    def tim_buoi_tap(self, ma_buoi_tap):
        for buoi in self.danh_sach_buoi_tap:
            if buoi.ma_buoi_tap == str(ma_buoi_tap):
                return buoi
        return None

    def cap_nhat_buoi_tap(self, ma_buoi_tap, **du_lieu):
        buoi = self.tim_buoi_tap(ma_buoi_tap)
        if buoi is None:
            return False
        buoi.cap_nhat_ket_qua(**du_lieu)
        self._dong_bo()
        return True

    def xoa_buoi_tap(self, ma_buoi_tap):
        buoi = self.tim_buoi_tap(ma_buoi_tap)
        if buoi is None:
            return False
        self.danh_sach_buoi_tap.remove(buoi)
        self._dong_bo()
        return True

    def loc_buoi_tap(self, ngay=None, mon_tap=None):
        ket_qua = self.danh_sach_buoi_tap
        if ngay:
            ket_qua = [b for b in ket_qua if b.ngay_tap == ngay]
        if mon_tap:
            ket_qua = [b for b in ket_qua if b.mon_tap.casefold() == mon_tap.casefold()]
        return list(ket_qua)

    def lay_thong_ke(self):
        self.thong_ke.cap_nhat_du_lieu(self.danh_sach_buoi_tap)
        return {
            "so_buoi": self.thong_ke.dem_so_buoi(),
            "tong_thoi_gian_phut": self.thong_ke.tinh_tong_thoi_gian(),
            "tong_diem": self.thong_ke.tinh_tong_diem(),
            "theo_mon": self.thong_ke.thong_ke_theo_mon(),
        }

    def luu_du_lieu(self):
        self.quan_ly_du_lieu.ghi_danh_sach_buoi_tap(
            self.danh_sach_buoi_tap, self.ten_file
        )

    def _dong_bo(self):
        self.thong_ke.cap_nhat_du_lieu(self.danh_sach_buoi_tap)
        self.luu_du_lieu()
