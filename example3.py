"""
    Function that accepts two lists of scores and a list of weights.
    The function returns a list of items where each item is a number of the sum of matching items
    in the same position for scores list multiplied by the number in the weights list in that same
    matching position.

    i.e result[0] = [ (scores1[0] + scores2[0]) * weights[0], ... ]

"""


def calculate_total_scores(scores1, scores2, weights):
    total_scores = []
    for i in range(len(scores1)):
        if len(scores1) == len(scores2) and len(scores1) == len(weights):
            total_scores.append((scores1[i] * weights[i]) + (scores2[i] * weights[i]))
        else:
            total_scores.append(0)
    return total_scores


# Test the function:
scores_1st = [66, 31, 72, 49, 68]
scores_2nd = [82, 61, 45, 71, 79]
score_weights = [2, 1, 1, 3, 3]

print(calculate_total_scores(scores_1st, scores_2nd, score_weights))



