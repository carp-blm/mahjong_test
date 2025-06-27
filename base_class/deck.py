# coding: utf-8
from typing import Any

from base_class.tile import Tile


class Haizan:  # 패산
    def __init__(self, tiles: list[Tile]):
        self.tiles = tiles

    def __len__(self):
        return len(self.tiles)

    def __getitem__(self, index: Any):
        return self.tiles[index]

    def __delitem__(self, index: Any):
        del self.tiles[index]

    # TODO: 패산의 수가 0이 되면, 해당 순을 마침과 함께 국을 종료한다.


class Wanpai:  # 왕패
    def __init__(self, tiles: list[Tile]):
        self.tiles = tiles[10:]
        self.doras = tiles[:5]
        self.ura_doras = tiles[5:10]

    def __len__(self):
        return len(self.tiles)

    def __getitem__(self, index: Any):
        return self.tiles[index]

    def __delitem__(self, index: Any):
        del self.tiles[index]

    # TODO: 왕패에서 한 장이 뽑힐 경우, 패산에서 한 장을 보충한다.
