from datetime import date
from muc_tieu import ChiSoCoThe


class HoSoNguoiDung:
    """Lưu hồ sơ cơ bản của người sử dụng ứng dụng."""

    def __init__(self, ma_nguoi_dung, ho_ten, tuoi, chieu_cao_cm, can_nang_kg):
        if not ma_nguoi_dung:
            raise ValueError("Mã người dùng không được để trống.")
        if not ho_ten or not ho_ten.strip():
            raise ValueError("Họ tên không được để trống.")
        if tuoi <= 0:
            raise ValueError("Tuổi phải lớn hơn 0.")
        if chieu_cao_cm <= 0 or can_nang_kg <= 0:
            raise ValueError("Chiều cao và cân nặng phải lớn hơn 0.")

        self.ma_nguoi_dung = str(ma_nguoi_dung)
        self.ho_ten = ho_ten.strip()
        self.tuoi = int(tuoi)
        self._chieu_cao_cm = float(chieu_cao_cm)
        self._can_nang_kg = float(can_nang_kg)
        self.lich_su_chi_so = []

    @property
    def chieu_cao_cm(self):
        return self._chieu_cao_cm

    @chieu_cao_cm.setter
    def chieu_cao_cm(self, gia_tri):
        if gia_tri <= 0:
            raise ValueError("Chiều cao phải lớn hơn 0.")
        self._chieu_cao_cm = float(gia_tri)

    @property
    def can_nang_kg(self):
        return self._can_nang_kg

    @can_nang_kg.setter
    def can_nang_kg(self, gia_tri):
        if gia_tri <= 0:
            raise ValueError("Cân nặng phải lớn hơn 0.")
        self._can_nang_kg = float(gia_tri)

    def tinh_bmi(self):
        chieu_cao_m = self._chieu_cao_cm / 100
        return round(self._can_nang_kg / (chieu_cao_m ** 2), 2)

    def cap_nhat_ho_so(self, ho_ten=None, tuoi=None, chieu_cao_cm=None, can_nang_kg=None):
        if ho_ten is not None:
            if not ho_ten.strip():
                raise ValueError("Họ tên không được để trống.")
            self.ho_ten = ho_ten.strip()
        if tuoi is not None:
            if tuoi <= 0:
                raise ValueError("Tuổi phải lớn hơn 0.")
            self.tuoi = int(tuoi)
        if chieu_cao_cm is not None:
            self.chieu_cao_cm = chieu_cao_cm
        if can_nang_kg is not None:
            self.can_nang_kg = can_nang_kg

    def ghi_nhan_chi_so(self, can_nang_kg, ngay=None, ghi_chu=""):
        chi_so = ChiSoCoThe(can_nang_kg, ngay or date.today().isoformat(), ghi_chu)
        self.lich_su_chi_so.append(chi_so)
        self.can_nang_kg = can_nang_kg
        return chi_so

    def hien_thi_thong_tin(self):
        return (
            f"Mã: {self.ma_nguoi_dung} | Họ tên: {self.ho_ten} | "
            f"Tuổi: {self.tuoi} | Chiều cao: {self.chieu_cao_cm} cm | "
            f"Cân nặng: {self.can_nang_kg} kg | BMI: {self.tinh_bmi()}"
        )

    def to_dict(self):
        return {
            "ma_nguoi_dung": self.ma_nguoi_dung,
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "chieu_cao_cm": self.chieu_cao_cm,
            "can_nang_kg": self.can_nang_kg,
            "lich_su_chi_so": [item.to_dict() for item in self.lich_su_chi_so],
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["ma_nguoi_dung"], data["ho_ten"], data["tuoi"],
            data["chieu_cao_cm"], data["can_nang_kg"]
        )
        obj.lich_su_chi_so = [
            ChiSoCoThe.from_dict(item) for item in data.get("lich_su_chi_so", [])
        ]
        return obj
