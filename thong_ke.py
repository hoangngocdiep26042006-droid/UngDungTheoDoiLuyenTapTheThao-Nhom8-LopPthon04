class ThongKeLuyenTap:
    """Tính toán thống kê từ danh sách buổi tập."""

    def __init__(self, danh_sach_buoi_tap=None):
        self.danh_sach_buoi_tap = list(danh_sach_buoi_tap or [])

    def cap_nhat_du_lieu(self, danh_sach_buoi_tap):
        self.danh_sach_buoi_tap = list(danh_sach_buoi_tap)

    def tinh_tong_thoi_gian(self, danh_sach=None):
        ds = self.danh_sach_buoi_tap if danh_sach is None else danh_sach
        return sum(b.thoi_luong for b in ds)

    def dem_so_buoi(self, danh_sach=None):
        ds = self.danh_sach_buoi_tap if danh_sach is None else danh_sach
        return len(ds)

    def tinh_tong_diem(self, danh_sach=None):
        ds = self.danh_sach_buoi_tap if danh_sach is None else danh_sach
        return round(sum(b.tinh_diem() for b in ds), 2)

    def thong_ke_theo_mon(self):
        ket_qua = {}
        for buoi in self.danh_sach_buoi_tap:
            ten_mon = buoi.mon_tap
            if ten_mon not in ket_qua:
                ket_qua[ten_mon] = {"so_buoi": 0, "tong_phut": 0, "tong_diem": 0}
            ket_qua[ten_mon]["so_buoi"] += 1
            ket_qua[ten_mon]["tong_phut"] += buoi.thoi_luong
            ket_qua[ten_mon]["tong_diem"] += buoi.tinh_diem()
        for thong_tin in ket_qua.values():
            thong_tin["tong_diem"] = round(thong_tin["tong_diem"], 2)
        return ket_qua

    def loc_theo_ngay(self, ngay):
        return [b for b in self.danh_sach_buoi_tap if b.ngay_tap == ngay]

    def loc_theo_mon(self, ten_mon):
        return [
            b for b in self.danh_sach_buoi_tap
            if b.mon_tap.casefold() == ten_mon.casefold()
        ]

    def tinh_muc_hoan_thanh(self, muc_tieu):
        if muc_tieu.don_vi == "phut":
            gia_tri = self.tinh_tong_thoi_gian()
        elif muc_tieu.don_vi == "buoi":
            gia_tri = self.dem_so_buoi()
        elif muc_tieu.don_vi == "diem":
            gia_tri = self.tinh_tong_diem()
        elif muc_tieu.don_vi == "km":
            gia_tri = sum(getattr(b, "quang_duong_km", 0) for b in self.danh_sach_buoi_tap)
        else:
            gia_tri = 0
        return muc_tieu.tinh_ti_le_hoan_thanh(gia_tri)
