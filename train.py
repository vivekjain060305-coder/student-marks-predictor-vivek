import csv
import json

x_values = []
y_values = []

with open("student_marks_dataset.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        x_values.append(float(row["hours"]))
        y_values.append(float(row["marks"]))

n = len(x_values)

x_mean = sum(x_values) / n
y_mean = sum(y_values) / n

numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
denominator = sum((x - x_mean) ** 2 for x in x_values)

slope = numerator / denominator
intercept = y_mean - slope * x_mean

model_data = {
    "slope": slope,
    "intercept": intercept
}

with open("model_params.json", "w") as file:
    json.dump(model_data, file)

print("Model trained and saved successfully!")
print("Slope:", slope)
print("Intercept:", intercept)