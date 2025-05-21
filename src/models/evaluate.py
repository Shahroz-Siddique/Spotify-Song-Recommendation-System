def precision_at_k(actual, predicted, k):
    actual_set = set(actual[:k])
    predicted_set = set(predicted[:k])
    return len(actual_set & predicted_set) / float(k)
