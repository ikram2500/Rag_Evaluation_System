from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="What do penguins eat?",
    actual_output=("Penguins mainly eat marine animals such as krill, fish, and squid.")
)

metric = AnswerRelevancyMetric(threshold=0.7)

metric.measure(test_case)

print("Score: ", metric.score)
print("Reason: ", metric.reason)
print("Passed: ", metric.is_successful())