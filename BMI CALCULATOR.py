import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numbers only for height and weight.")
        return

    if height <= 0 or weight <= 0:
        messagebox.showerror("Invalid Input", "Height and weight must be greater than zero.")
        return

    bmi = weight / ((height/100) ** 2)

    if bmi < 18.5:
        category = "Underweight"
        suggestion = "Consider eating more nutrient-rich foods and exercising to gain healthy weight; consult a doctor if needed."
    elif bmi < 25:
        category = "Normal weight"
        suggestion = "Maintain a balanced diet, stay active, and continue healthy lifestyle habits to keep your weight in a normal range."
    elif bmi < 30:
        category = "Overweight"
        suggestion = "Consider adopting a balanced diet and regular exercise to gradually lose weight and improve overall health."
    else:
        category = "Obese"
        suggestion = "It’s important to seek medical advice and adopt a healthy diet and regular physical activity to manage your weight safely."

    result_label.config(text=f"BMI: {bmi:.2f}\n\nCategory: {category}\n\nSuggestion: {suggestion}")

# --- GUI Setup ---
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Title Label
tk.Label(root, text="BMI Calculator", font=("Arial", 16)).pack(pady=10)

# Height input
tk.Label(root, text="Enter height (cm):", font=("Arial", 10)).pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Weight input
tk.Label(root, text="Enter weight (kg):", font=("Arial", 10)).pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Calculate Button
tk.Button(root, text="Calculate BMI", font=("Arial", 10), command=calculate_bmi).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Start the GUI loop
root.mainloop()