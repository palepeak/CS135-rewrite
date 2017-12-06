"""
# Created on Sep 14, 2017
# @author: bobbywang
"""


class Card():
    def __init__(self, cardstrength, cardcolor):
        self.strength = cardstrength
        self.color = cardcolor

    def gets(self):
        return self.strength

    def getc(self):
        return self.color


class Hand():
    def __init__(self, card1, card2, card3):
        self.c1 = card1
        self.c2 = card2
        self.c3 = card3

    def max(self):
        if (self.c1.strength >= self.c2.strength) and (self.c1.strength >= self.c3.strength):
            return self.c1.strength
        if (self.c2.strength >= self.c1.strength) and (self.c2.strength >= self.c3.strength):
            return self.c2.strength
        if (self.c3.strength >= self.c2.strength) and (self.c3.strength >= self.c1.strength):
            return self.c3.strength

    def min(self):
        if (self.c1.strength <= self.c2.strength) and (self.c1.strength <= self.c3.strength):
            return self.c1.strength
        if (self.c2.strength <= self.c1.strength) and (self.c2.strength <= self.c3.strength):
            return self.c2.strength
        if (self.c3.strength <= self.c2.strength) and (self.c3.strength <= self.c1.strength):
            return self.c3.strength

    def getc1(self):
        return self.c1

    def getc2(self):
        return self.c2

    def getc3(self):
        return self.c3


rawhandinfo = raw_input("")
card1, card2, card3 = rawhandinfo.split(",")
card1s, card1c = card1.split("-")
card2s, card2c = card2.split("-")
card3s, card3c = card3.split("-")

hand1 = Hand(Card(int(card1s), card1c),
             Card(int(card2s), card2c),
             Card(int(card3s), card3c))

rawhandinfo = raw_input("")
card1, card2, card3 = rawhandinfo.split(",")
card1s, card1c = card1.split("-")
card2s, card2c = card2.split("-")
card3s, card3c = card3.split("-")

hand2 = Hand(Card(int(card1s), card1c),
             Card(int(card2s), card2c),
             Card(int(card3s), card3c))


def run(hand):
    if ((hand.getc1().gets() + hand.getc2().gets() + hand.getc3().gets()) / 3) == ((hand.max() + hand.min()) / 2):
        if (hand.max() - hand.min() == 2):
            return 1
        else:
            return 0
    else:
        return 0


def color(hand):
    if hand.getc1().getc() == hand.getc2().getc() and hand.getc2().getc() == hand.getc3().getc():
        return 1
    else:
        return 0


def tok(hand):
    if hand.getc1().gets() == hand.getc2().gets() and hand.getc2().gets() == hand.getc3().gets():
        return 1
    else:
        return 0


def cr(hand):
    if (run(hand) + color(hand)) == 2:
        return 1
    else:
        return 0


def scorecalc(hand):
    return ((run(hand) * 100) +
            (color(hand) * 1000) +
            (tok(hand) * 10000) +
            (cr(hand) * 100000) +
            hand.getc1().gets() +
            hand.getc2().gets() +
            hand.getc3().gets())


def battle(hand1, hand2):
    if scorecalc(hand1) >= scorecalc(hand2):
        print ("player 1")
    else:
        print ("player 2")


battle(hand1, hand2)