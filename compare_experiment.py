import json

with open("experiment_v1.jsonl", "r", encoding="utf-8") as file:
    k1 = json.load(file)

with open("experiment_v2.json2", "r", encoding="utf-8") as file:
    k2 = json.load(file)

with open("experiment_v3.json3", "r", encoding="utf-8") as file:
    k3 = json.load(file)


print("\n========== ALL EXPERIMENT ==========\n")

print(f"{'Metric':<22} {'K=1':<15} {'K=2':<15} {'K=3':<15} {'Change':<10}")
print("-" * 80)

for metric in k1["metrics"]:

    k1_score = k1["metrics"][metric]
    k2_score = k2["metrics"][metric]
    k3_score = k3["metrics"][metric]

    print(
        f"{metric.replace('_', ' ').title():<22} "
        f"{k1_score:<15.2f} "
        f"{k2_score:<15.2f} "
        f"{k3_score:<15.2f} "
        f"{(k3_score - k1_score):<10.2f}"
    )
