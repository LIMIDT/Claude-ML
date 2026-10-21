"""Local scorer for Practice_1.

Usage:
    python score.py [pred.csv]
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
pred_path = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "pred.csv"

if not pred_path.exists():
    raise SystemExit(f"找不到预测文件: {pred_path}")

pred = pd.read_csv(pred_path)
labels = pd.read_csv(BASE / "test_labels.csv")
train = pd.read_csv(BASE / "bike_train.csv")

y_true = labels["target"].values
y_pred = pred["target"].values

if len(y_pred) != len(y_true):
    raise SystemExit(f"预测行数不对: {len(y_pred)} != {len(y_true)}")

mse = np.mean((y_true - y_pred) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_true - y_pred))
r2 = 1 - np.sum((y_true - y_pred) ** 2) / np.sum((y_true - y_true.mean()) ** 2)
baseline_rmse = np.sqrt(np.mean((y_true - train["target"].mean()) ** 2))

print(f"MSE  = {mse:.2f}")
print(f"RMSE = {rmse:.2f}   (越小越好)")
print(f"MAE  = {mae:.2f}")
print(f"R^2  = {r2:.4f}")
print(f"baseline RMSE (predict train mean) = {baseline_rmse:.2f}")
print(f"improvement over baseline = {baseline_rmse - rmse:.2f}")
