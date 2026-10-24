class MonTap:
    """Thông tin chung về một môn thể thao."""

    def __init__(self, ma_mon, ten_mon, mo_ta=""):
        if not ma_mon or not ten_mon or not ten_mon.strip():
            raise ValueError("Mã môn và tên môn không được để trống.")
        self.ma_mon = str(ma_mon)
        self.ten_mon = ten_mon.strip()
        self.mo_ta = mo_ta

    def hien_thi_thong_tin(self):
        return f"{self.ma_mon} - {self.ten_mon}: {self.mo_ta}"

    def to_dict(self):
        return {"ma_mon": self.ma_mon, "ten_mon": self.ten_mon, "mo_ta": self.mo_ta}

    @classmethod
    def from_dict(cls, data):
        return cls(data["ma_mon"], data["ten_mon"], data.get("mo_ta", ""))
