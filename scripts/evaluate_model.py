from src.models.evaluate import precision_at_k

actual = ['song1', 'song2', 'song3']
predicted = ['song2', 'song4', 'song1']
print("Precision@3:", precision_at_k(actual, predicted, 3))
