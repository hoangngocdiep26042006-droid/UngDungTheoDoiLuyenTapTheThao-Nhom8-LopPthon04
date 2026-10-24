from datetime import date, datetime

from buoi_tap import BuoiTapChayBo, BuoiTapDapXe, BuoiTapGym
from du_lieu import QuanLyDuLieu
from quan_ly import QuanLyLuyenTap
from muc_tieu import MucTieu


def hien_thi_menu():
    print("\n===== ỨNG DỤNG THEO DÕI LUYỆN TẬP =====")
    print("1. Hiển thị các buổi tập")
    print("2. Thêm buổi chạy bộ")
    print("3. Thêm buổi đạp xe")
    print("4. Thêm buổi gym")
    print("5. Lọc buổi tập theo ngày")
    print("6. Lọc buổi tập theo môn")
    print("7. Xem thống kê")
    print("8. Tính tiến độ mục tiêu thời gian")
    print("0. Lưu dữ liệu và thoát")


def nhap_so_nguyen(thong_bao, toi_thieu=0):
    while True:
        try:
            gia_tri = int(input(thong_bao))
            if gia_tri < toi_thieu:
                print(f"Vui lòng nhập số nguyên >= {toi_thieu}.")
                continue
            return gia_tri
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")


def nhap_so_thuc(thong_bao, toi_thieu=0):
    while True:
        try:
            gia_tri = float(input(thong_bao))
            if gia_tri < toi_thieu:
                print(f"Vui lòng nhập số >= {toi_thieu}.")
                continue
            return gia_tri
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập số.")


def nhap_ngay():
    while True:
        ngay = input("Ngày tập (YYYY-MM-DD, Enter = hôm nay): ").strip()
        if not ngay:
            return date.today().isoformat()
        try:
            datetime.strptime(ngay, "%Y-%m-%d")
            return ngay
        except ValueError:
            print("Ngày không đúng định dạng. Ví dụ hợp lệ: 2026-10-24")


def nhap_cuong_do():
    while True:
        cuong_do = input("Cường độ (Nhẹ/Vừa/Cao): ").strip().capitalize()
        if cuong_do in {"Nhẹ", "Vừa", "Cao"}:
            return cuong_do
        print("Vui lòng nhập đúng một trong ba mức: Nhẹ, Vừa hoặc Cao.")


def in_danh_sach(danh_sach):
    if not danh_sach:
        print("Không có buổi tập phù hợp.")
        return
    print("\n--- DANH SÁCH BUỔI TẬP ---")
    for buoi in danh_sach:
        print(buoi.hien_thi_thong_tin())
        if getattr(buoi, "ghi_chu", ""):
            print(f"   Ghi chú: {buoi.ghi_chu}")


def them_buoi_tap(lua_chon, quan_ly):
    ma = input("Mã buổi tập: ").strip()
    if not ma:
        print("Mã buổi tập không được để trống.")
        return

    ngay = nhap_ngay()
    thoi_luong = nhap_so_nguyen("Thời lượng (phút): ", 1)
    cuong_do = nhap_cuong_do()
    ghi_chu = input("Ghi chú (có thể bỏ trống): ").strip()

    try:
        if lua_chon == "2":
            km = nhap_so_thuc("Quãng đường chạy (km): ")
            buoi = BuoiTapChayBo(
                ma, ngay_tap=ngay, thoi_luong=thoi_luong,
                cuong_do=cuong_do, ghi_chu=ghi_chu,
                quang_duong_km=km
            )
        elif lua_chon == "3":
            km = nhap_so_thuc("Quãng đường đạp xe (km): ")
            buoi = BuoiTapDapXe(
                ma, ngay_tap=ngay, thoi_luong=thoi_luong,
                cuong_do=cuong_do, ghi_chu=ghi_chu,
                quang_duong_km=km
            )
        else:
            so_hiep = nhap_so_nguyen("Số hiệp: ")
            so_lan = nhap_so_nguyen("Số lần lặp: ")
            ta = nhap_so_thuc("Khối lượng tạ (kg): ")
            buoi = BuoiTapGym(
                ma, ngay_tap=ngay, thoi_luong=thoi_luong,
                cuong_do=cuong_do, ghi_chu=ghi_chu,
                so_hiep=so_hiep, so_lan_lap=so_lan,
                khoi_luong_ta_kg=ta
            )

        quan_ly.them_buoi_tap(buoi)  # Hàm này tự lưu dữ liệu JSON.
        print("\nĐã thêm buổi tập thành công!")
        print("Thông tin vừa nhập:")
        print(buoi.hien_thi_thong_tin())
        print("Dữ liệu đã được lưu vào data/buoi_tap.json.")
    except (ValueError, TypeError) as loi:
        print("Không thể thêm buổi tập:", loi)


def main():
    du_lieu = QuanLyDuLieu("data")
    quan_ly = QuanLyLuyenTap(du_lieu)

    print("Đã tải", len(quan_ly.danh_sach_buoi_tap), "buổi tập từ file JSON.")

    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng: ").strip()

        if lua_chon == "1":
            in_danh_sach(quan_ly.danh_sach_buoi_tap)

        elif lua_chon in {"2", "3", "4"}:
            them_buoi_tap(lua_chon, quan_ly)

        elif lua_chon == "5":
            ngay = input("Nhập ngày cần lọc (YYYY-MM-DD): ").strip()
            in_danh_sach(quan_ly.loc_buoi_tap(ngay=ngay))

        elif lua_chon == "6":
            print("Môn hợp lệ: Chạy bộ, Đạp xe, Gym")
            mon = input("Nhập môn tập: ").strip()
            in_danh_sach(quan_ly.loc_buoi_tap(mon_tap=mon))

        elif lua_chon == "7":
            tk = quan_ly.lay_thong_ke()
            print("\n--- THỐNG KÊ LUYỆN TẬP ---")
            print(f"Số buổi tập: {tk['so_buoi']}")
            print(f"Tổng thời gian: {tk['tong_thoi_gian_phut']} phút")
            print(f"Tổng điểm: {tk['tong_diem']}")
            print("Thống kê theo môn:")
            if not tk["theo_mon"]:
                print("Chưa có dữ liệu.")
            for mon, data in tk["theo_mon"].items():
                print(f"- {mon}: {data['so_buoi']} buổi, "
                      f"{data['tong_phut']} phút, {data['tong_diem']} điểm")

        elif lua_chon == "8":
            tong_phut = quan_ly.lay_thong_ke()["tong_thoi_gian_phut"]
            muc_tieu_phut = nhap_so_thuc("Nhập mục tiêu tổng thời gian (phút): ", 1)
            muc_tieu = MucTieu("MT-BAN-NHAP", "Mục tiêu thời gian", muc_tieu_phut, "phut")
            ti_le = muc_tieu.tinh_ti_le_hoan_thanh(tong_phut)
            print(f"Đã tập: {tong_phut} phút / mục tiêu {muc_tieu_phut:g} phút")
            print(f"Tiến độ hoàn thành: {ti_le}%")

        elif lua_chon == "0":
            quan_ly.luu_du_lieu()
            print("Đã lưu dữ liệu. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 8.")


if __name__ == "__main__":
    main()
