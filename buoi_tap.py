from abc import ABC, abstractmethod
from datetime import date


class PhuongPhapTinhDiem(ABC):
    """Lớp trừu tượng quy định các buổi tập phải có cách tính điểm."""

    @abstractmethod
    def tinh_diem(self):
        """Trả về điểm luyện tập không âm."""
        raise NotImplementedError


class BuoiTap(PhuongPhapTinhDiem):
    """Lớp cơ sở cho một buổi tập."""

    def __init__(self, ma_buoi_tap, ngay_tap=None, mon_tap="Chưa xác định",
                 thoi_luong=0, cuong_do="Vừa", ghi_chu=""):
        if not ma_buoi_tap:
            raise ValueError("Mã buổi tập không được để trống.")
        if int(thoi_luong) < 0:
            raise ValueError("Thời lượng không được âm.")
        if cuong_do not in {"Nhẹ", "Vừa", "Cao"}:
            raise ValueError("Cường độ phải là Nhẹ, Vừa hoặc Cao.")

        self.ma_buoi_tap = str(ma_buoi_tap)
        self.ngay_tap = ngay_tap or date.today().isoformat()
        self.mon_tap = mon_tap
        self.thoi_luong = int(thoi_luong)  # phút
        self.cuong_do = cuong_do
        self.ghi_chu = ghi_chu

    def tinh_diem(self):
        he_so = {"Nhẹ": 1, "Vừa": 1.5, "Cao": 2}
        return round(self.thoi_luong * he_so[self.cuong_do], 2)

    def cap_nhat_ket_qua(self, ngay_tap=None, mon_tap=None, thoi_luong=None,
                         cuong_do=None, ghi_chu=None):
        if thoi_luong is not None:
            if int(thoi_luong) < 0:
                raise ValueError("Thời lượng không được âm.")
            self.thoi_luong = int(thoi_luong)
        if cuong_do is not None:
            if cuong_do not in {"Nhẹ", "Vừa", "Cao"}:
                raise ValueError("Cường độ phải là Nhẹ, Vừa hoặc Cao.")
            self.cuong_do = cuong_do
        if ngay_tap is not None:
            self.ngay_tap = ngay_tap
        if mon_tap is not None:
            self.mon_tap = mon_tap
        if ghi_chu is not None:
            self.ghi_chu = ghi_chu

    def hien_thi_thong_tin(self):
        return (
            f"{self.ma_buoi_tap} | {self.ngay_tap} | {self.mon_tap} | "
            f"{self.thoi_luong} phút | {self.cuong_do} | {self.tinh_diem()} điểm"
        )

    def to_dict(self):
        return {
            "loai": self.__class__.__name__,
            "ma_buoi_tap": self.ma_buoi_tap,
            "ngay_tap": self.ngay_tap,
            "mon_tap": self.mon_tap,
            "thoi_luong": self.thoi_luong,
            "cuong_do": self.cuong_do,
            "ghi_chu": self.ghi_chu,
        }


class BuoiTapChayBo(BuoiTap):
    def __init__(self, *args, quang_duong_km=0, **kwargs):
        super().__init__(*args, mon_tap="Chạy bộ", **kwargs)
        if float(quang_duong_km) < 0:
            raise ValueError("Quãng đường không được âm.")
        self.quang_duong_km = float(quang_duong_km)

    def tinh_diem(self):
        return round(super().tinh_diem() + self.quang_duong_km * 2, 2)

    def to_dict(self):
        data = super().to_dict()
        data["quang_duong_km"] = self.quang_duong_km
        return data


class BuoiTapDapXe(BuoiTap):
    def __init__(self, *args, quang_duong_km=0, **kwargs):
        super().__init__(*args, mon_tap="Đạp xe", **kwargs)
        if float(quang_duong_km) < 0:
            raise ValueError("Quãng đường không được âm.")
        self.quang_duong_km = float(quang_duong_km)

    def tinh_diem(self):
        return round(super().tinh_diem() + self.quang_duong_km, 2)

    def to_dict(self):
        data = super().to_dict()
        data["quang_duong_km"] = self.quang_duong_km
        return data


class BuoiTapGym(BuoiTap):
    def __init__(self, *args, so_hiep=0, so_lan_lap=0, khoi_luong_ta_kg=0, **kwargs):
        super().__init__(*args, mon_tap="Gym", **kwargs)
        if min(int(so_hiep), int(so_lan_lap), float(khoi_luong_ta_kg)) < 0:
            raise ValueError("Thông số tập gym không được âm.")
        self.so_hiep = int(so_hiep)
        self.so_lan_lap = int(so_lan_lap)
        self.khoi_luong_ta_kg = float(khoi_luong_ta_kg)

    def tinh_diem(self):
        return round(
            super().tinh_diem()
            + self.so_hiep * 2
            + self.so_lan_lap * 0.1
            + self.khoi_luong_ta_kg * 0.2, 2
        )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "so_hiep": self.so_hiep,
            "so_lan_lap": self.so_lan_lap,
            "khoi_luong_ta_kg": self.khoi_luong_ta_kg,
        })
        return data


def buoi_tap_from_dict(data):
    """Tạo đúng loại đối tượng từ dữ liệu JSON."""
    loai = data.get("loai", "BuoiTap")
    chung = {
        "ma_buoi_tap": data["ma_buoi_tap"],
        "ngay_tap": data.get("ngay_tap"),
        "thoi_luong": data.get("thoi_luong", 0),
        "cuong_do": data.get("cuong_do", "Vừa"),
        "ghi_chu": data.get("ghi_chu", ""),
    }
    if loai == "BuoiTapChayBo":
        return BuoiTapChayBo(**chung, quang_duong_km=data.get("quang_duong_km", 0))
    if loai == "BuoiTapDapXe":
        return BuoiTapDapXe(**chung, quang_duong_km=data.get("quang_duong_km", 0))
    if loai == "BuoiTapGym":
        return BuoiTapGym(
            **chung, so_hiep=data.get("so_hiep", 0),
            so_lan_lap=data.get("so_lan_lap", 0),
            khoi_luong_ta_kg=data.get("khoi_luong_ta_kg", 0)
        )
    return BuoiTap(
        **chung, mon_tap=data.get("mon_tap", "Chưa xác định")
    )
