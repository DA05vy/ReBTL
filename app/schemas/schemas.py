from typing import Optional

class Human:
    id: str
    name: str
    he_so_luong: float
    luong_co_ban: int
    """
        Khởi tạo đối tượng Human với các thông tin cơ bản
    """

    def __init__(self, id: str, name: str, he_so_luong: float, luong_co_ban: int) -> None:
        self.id = id
        self.name = name
        self.he_so_luong = he_so_luong
        self.luong_co_ban = luong_co_ban

    def tinh_luong(self) -> float:
        """
            Tính lương cơ bản (được tính khác nhau tùy loại nhân viên)
        """
        return self.luong_co_ban * self.he_so_luong


class Staff(Human):
    chuc_vu: str

    def __init__(self, id: str, name: str, he_so_luong: float, luong_co_ban: int, chuc_vu: int) -> None:
        super().__init__(id, name, he_so_luong, luong_co_ban)
        self.chuc_vu = str(chuc_vu)

    def tinh_luong(self) -> float:
        return super().tinh_luong() * 0.5


class Manager(Human):
    chuc_danh: str

    def __init__(self, id: str, name: str, he_so_luong: float, luong_co_ban: int, chuc_danh: str) -> None:
        super().__init__(id, name, he_so_luong, luong_co_ban)
        self.chuc_danh = chuc_danh

    def tinh_luong(self) -> float:
        return super().tinh_luong() * 1


