def latest(scores):
    for x in scores:
        return scores[-1]

def personal_best(scores):
    for x in scores:
        return max(scores)


def personal_top_three(scores):
    scores.sort(reverse = True)

    return scores[0:3]

        
