import csv
import json
import os
from buoi_tap import buoi_tap_from_dict


class QuanLyDuLieu:
    """Đọc/ghi dữ liệu JSON và CSV. Các đường dẫn được truyền vào khi tạo đối tượng."""

    def __init__(self, thu_muc_du_lieu="data"):
        self.thu_muc_du_lieu = thu_muc_du_lieu
        os.makedirs(self.thu_muc_du_lieu, exist_ok=True)

    def _duong_dan(self, ten_file):
        return os.path.join(self.thu_muc_du_lieu, ten_file)

    def doc_json(self, ten_file, mac_dinh=None):
        duong_dan = self._duong_dan(ten_file)
        if not os.path.exists(duong_dan):
            return [] if mac_dinh is None else mac_dinh
        with open(duong_dan, "r", encoding="utf-8") as f:
            return json.load(f)

    def ghi_json(self, ten_file, du_lieu):
        with open(self._duong_dan(ten_file), "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)

    def doc_csv(self, ten_file):
        duong_dan = self._duong_dan(ten_file)
        if not os.path.exists(duong_dan):
            return []
        with open(duong_dan, "r", encoding="utf-8-sig", newline="") as f:
            return list(csv.DictReader(f))

    def ghi_csv(self, ten_file, danh_sach, fieldnames=None):
        danh_sach = list(danh_sach)
        if fieldnames is None:
            fieldnames = list(danh_sach[0].keys()) if danh_sach else []
        with open(self._duong_dan(ten_file), "w", encoding="utf-8-sig", newline="") as f:
            if not fieldnames:
                return
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(danh_sach)

    def doc_danh_sach_buoi_tap(self, ten_file="buoi_tap.json"):
        du_lieu = self.doc_json(ten_file, [])
        return [buoi_tap_from_dict(item) for item in du_lieu]

    def ghi_danh_sach_buoi_tap(self, danh_sach_buoi_tap, ten_file="buoi_tap.json"):
        self.ghi_json(ten_file, [buoi.to_dict() for buoi in danh_sach_buoi_tap])
