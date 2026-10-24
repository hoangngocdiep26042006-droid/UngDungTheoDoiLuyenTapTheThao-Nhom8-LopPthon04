from datetime import date


class NhacLich:
    """Quản lý các lịch tập dự kiến; chưa gửi thông báo hệ điều hành."""

    def __init__(self):
        self.danh_sach_lich = []

    def them_lich_nhac(self, ngay, gio, noi_dung):
        if not ngay or not gio or not noi_dung:
            raise ValueError("Ngày, giờ và nội dung nhắc không được để trống.")
        lich = {"ngay": ngay, "gio": gio, "noi_dung": noi_dung, "da_hoan_thanh": False}
        self.danh_sach_lich.append(lich)
        return lich

    def danh_sach_theo_ngay(self, ngay):
        return [lich for lich in self.danh_sach_lich if lich["ngay"] == ngay]

    def danh_sach_hom_nay(self):
        return self.danh_sach_theo_ngay(date.today().isoformat())

    def danh_dau_hoan_thanh(self, ngay, gio, noi_dung):
        for lich in self.danh_sach_lich:
            if (lich["ngay"], lich["gio"], lich["noi_dung"]) == (ngay, gio, noi_dung):
                lich["da_hoan_thanh"] = True
                return True
        return False

    def to_list(self):
        return [lich.copy() for lich in self.danh_sach_lich]
