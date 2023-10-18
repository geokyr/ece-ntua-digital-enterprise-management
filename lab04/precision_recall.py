# function to print the results
def print_results(identifier, float_precision):
    print(identifier)
    print(f"- Precision: {round(precision, float_precision)}")
    print(f"- Recall: {round(recall, float_precision)}")
    print(f"- F-Measure: {round(fmeasure, float_precision)}")

# search results statistics
tp = 18
fp = 16
fn = 350

# calculate precision, recall and fmeasure
precision = tp / (tp + fp)
recall = tp / (tp + fn)
fmeasure = 2 * precision * recall / (precision + recall)

identifiers = ["Metrics", "\nRounded Metrics"]
float_precisions = [10, 3]

for identifier, float_precision in zip(identifiers, float_precisions):
    print_results(identifier, float_precision)
