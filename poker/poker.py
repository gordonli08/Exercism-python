from collections import defaultdict

ranks = dict(zip(['2','3','4','5','6','7','8','9','10','J','Q','K','A'], range(2,15)))

def best_hands(hands):
    hand_dict = defaultdict()
    for hand in hands:
        #parse the hand into tuples
        p_hand = [(card[:-1], card[-1]) for card in  hand.split()]
        #transform the hand into ranks of each card 2-14
        hand_ranks = [ranks[num] for num, suit in p_hand]
        #case in which straight starts with ace
        if sorted(hand_ranks) == [2,3,4,5,14]:
            hand_ranks = [5,4,3,2,1]
        #construct the counts to calculate the poker hands and the ordered tuple for hand ranks
        hand_grouped = sorted([(hand_ranks.count(i),i) for i in set(hand_ranks)], reverse=True)
        counts, number = zip(*hand_grouped)

        straight = (len(counts) == 5 and max(number)-min(number) == 4)
        flush = len(set([suit for num, suit in p_hand])) == 1
        if straight and flush:
            hand_dict[hand] = (8, number)
        elif counts == (4,1):
            hand_dict[hand] = (7, number)
        elif counts == (3,2):
            hand_dict[hand] = (6, number)
        elif flush:
            hand_dict[hand] = (5, number)
        elif straight:
            hand_dict[hand] = (4, number)
        elif counts == (3, 1, 1):
            hand_dict[hand] = (3, number)
        elif counts == (2, 2, 1):
            hand_dict[hand] = (2, number)
        elif counts == (2, 1, 1, 1):
            hand_dict[hand] = (1, number)
        else:
            hand_dict[hand] = (0, number)

    currmax = max(hand_dict.values())
    return [hand_s for hand_s, val in hand_dict.items() if val == currmax]

