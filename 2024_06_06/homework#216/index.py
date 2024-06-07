import tkinter as tk
from tkinter import messagebox

# 計算 BMI 的函數
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height/100) ** 2
        messagebox.showinfo("BMI 結果", f"您的 BMI 是 {bmi:.2f}")
    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入有效的數字。")

# 建立主視窗
root = tk.Tk()
root.title("BMI 計算器")

# 標籤和輸入框
label_height = tk.Label(root, text="身高 (cm):")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

label_weight = tk.Label(root, text="體重 (kg):")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

# 計算按鈕
button_calculate = tk.Button(root, text="計算 BMI", command=calculate_bmi)
button_calculate.pack()

# 主迴圈
root.mainloop()
