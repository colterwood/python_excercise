#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def winner_is(game_round):
    """
    Finds the winner of a hand of poker, up to max 10 players.
    
    Arguments:
        game_round (dict): A dictionary where keys are player names, and values are their hands.
        
    Returns:
        The name of the winner as a string
    """
    
    hand_rankings = [
        "High Card", "Pair", "Two Pair", "Three of a Kind", "Straight",
        "Flush", "Full House", "Four of a Kind", "Straight Flush",
        "Royal Flush"
        ]

    def hand_rank_value(hand):
        """Returns the rank of a players hand"""
        rank = poker_hand_ranking(hand)
        return hand_rankings.index(rank)

    # Determine which player had the best hand.
    winner = max(game_round, key=lambda player: hand_rank_value(game_round[player]))
    return winner

    
    
round_1 = {"John" : ["As", "Ks", "Js", "4s", "2s"],
        "Peter" : ["5d", "6d", "7d", "9d", "Ts"],
        "Colter": ["9d", "Kd", "Jd", "Td", "Qd"],
        "Chelsea": ["Ah", "Kh", "Jh", "Th", "Qh"]
          }

winner = winner_is(round_1)
winning_hand = round_1[winner]
winning_hand_name = poker_hand_ranking(winning_hand)

print(f"The winner of the round is {winner_is(round_1)}, with a {winning_hand_name}!")

