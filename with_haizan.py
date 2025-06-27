# coding: utf-8
import random
from base_class.deck import Haizan, Wanpai
from base_class.tile import Tile


# 패산 생성
def generate_haizan() -> Haizan:
    haizan = []

    for suit in ["만", "통", "삭"]:
        for num in range(1, 10):
            for _ in range(4):
                haizan.append(Tile(suit, num))

    for suit in ["풍"]:
        for num in range(1, 5):
            for _ in range(4):
                haizan.append(Tile(suit, num))

    for suit in ["삼원"]:
        for num in range(1, 4):
            for _ in range(4):
                haizan.append(Tile(suit, num))

    random.shuffle(haizan)

    return Haizan(haizan)


# 패산 뒤 14장을 사용해 왕패 생성, 다시 섞는다
def generate_wanpai(haizan: Haizan) -> Wanpai:
    wanpai = haizan[:-14]
    random.shuffle(wanpai)

    return Wanpai(wanpai)


# 배패
def draw_haipai(haizan: Haizan) -> list[Tile]:
    haipai = haizan[0:12]

    del haizan[0:12]

    return haipai


# 손패 정리 순서
def tile_sort_key(tile: Tile) -> tuple[int, int]:
    suit_order = {"만": 0,
                  "통": 1,
                  "삭": 2,
                  "풍": 3,
                  "삼원": 4}

    return suit_order[tile.suit], tile.number


# 손패 정리
def sort_tiles(tiles: list[Tile]) -> list[Tile]:
    return sorted(tiles,
                  key=tile_sort_key)


# 도라 표시패 (도라 5개, 뒷도라 5개) -> Wanpai Method로


if __name__ == "__main__":
    deck_arg = generate_haizan()
    king_arg = generate_wanpai(deck_arg)
    hand_arg = draw_haipai(deck_arg)
    hand_sorted_arg = sort_tiles(hand_arg)
    print([h() for h in hand_sorted_arg])

    dora = king_arg.doras
    print(f"도라 표시패: [{dora[0]}]")
    print(f"뒷도라 표시패: [{dora[1]}]")
