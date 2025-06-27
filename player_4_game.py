# coding: utf-8
from test._mtest.with_haizan import generate_deck, draw_initial_hand, sort_tiles


def player_turn(hand, deck):
    input(f"내 차례. 엔터를 눌러 한 장을 뽑습니다. (남은 패산: {len(deck)})")

    drawn_tile = deck.pop()
    print(f"현재 패: {[h() for h in hand]} + {[drawn_tile()]}")


if __name__ == "__main__":
    d, k = generate_deck()
    h = draw_initial_hand(d)
    h = sort_tiles(h)
    player_turn(h, d)

