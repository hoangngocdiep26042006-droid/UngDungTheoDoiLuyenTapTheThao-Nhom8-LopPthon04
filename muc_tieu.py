from datetime import date


class ChiSoCoThe:
    """Một lần ghi nhận chỉ số cơ thể."""

    def __init__(self, can_nang_kg, ngay=None, ghi_chu=""):
        if float(can_nang_kg) <= 0:
            raise ValueError("Cân nặng phải lớn hơn 0.")
        self.can_nang_kg = float(can_nang_kg)
        self.ngay = ngay or date.today().isoformat()
        self.ghi_chu = ghi_chu

    def to_dict(self):
        return {
            "can_nang_kg": self.can_nang_kg,
            "ngay": self.ngay,
            "ghi_chu": self.ghi_chu,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["can_nang_kg"], data.get("ngay"), data.get("ghi_chu", ""))


class MucTieu:
    """Mục tiêu luyện tập theo tổng thời gian, số buổi hoặc quãng đường."""

    DON_VI_HOP_LE = {"phut", "buoi", "km", "diem"}

    def __init__(self, ma_muc_tieu, ten_muc_tieu, gia_tri_muc_tieu,
                 don_vi="phut", han_hoan_thanh=None):
        if not ma_muc_tieu:
            raise ValueError("Mã mục tiêu không được để trống.")
        if not ten_muc_tieu or not ten_muc_tieu.strip():
            raise ValueError("Tên mục tiêu không được để trống.")
        if float(gia_tri_muc_tieu) <= 0:
            raise ValueError("Giá trị mục tiêu phải lớn hơn 0.")
        if don_vi not in self.DON_VI_HOP_LE:
            raise ValueError(f"Đơn vị phải thuộc: {', '.join(sorted(self.DON_VI_HOP_LE))}")

        self.ma_muc_tieu = str(ma_muc_tieu)
        self.ten_muc_tieu = ten_muc_tieu.strip()
        self.gia_tri_muc_tieu = float(gia_tri_muc_tieu)
        self.don_vi = don_vi
        self.han_hoan_thanh = han_hoan_thanh

    def tinh_ti_le_hoan_thanh(self, gia_tri_hien_tai):
        if self.gia_tri_muc_tieu == 0:
            return 0.0
        return round(min(float(gia_tri_hien_tai) / self.gia_tri_muc_tieu * 100, 100), 2)

    def kiem_tra_hoan_thanh(self, gia_tri_hien_tai):
        return float(gia_tri_hien_tai) >= self.gia_tri_muc_tieu

    def to_dict(self):
        return {
            "ma_muc_tieu": self.ma_muc_tieu,
            "ten_muc_tieu": self.ten_muc_tieu,
            "gia_tri_muc_tieu": self.gia_tri_muc_tieu,
            "don_vi": self.don_vi,
            "han_hoan_thanh": self.han_hoan_thanh,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["ma_muc_tieu"], data["ten_muc_tieu"],
            data["gia_tri_muc_tieu"], data.get("don_vi", "phut"),
            data.get("han_hoan_thanh")
        )
