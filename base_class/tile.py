# coding: utf-8
class Tile:
    def __init__(self, suit: str, number: int):
        self.suit = suit  # 만, 통, 삭, 삼원, 풍
        self.number = number  # 1 ~ 9 (삼원패: 백 1, 발 2, 중 3 / 풍패: 동 1 남 2 서 3 북 4)

    def __str__(self):
        if self.suit in ["만", "통", "삭"]:
            return f"{self.number}{self.suit}"  # 9만
        elif self.suit in ["풍"]:
            return ["동", "남", "서", "북"][self.number - 1]
        elif self.suit in ["삼원"]:
            return ["백", "발", "중"][self.number - 1]

    def __call__(self):
        return str(self)


if __name__ == "__main__":
    t = Tile("풍", 2)
    print(t)
