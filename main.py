import tkinter as tk
from tkinter import ttk

class UnitConverter:
    def __init__(self,root):
        self.root = root
        self.root.title("Unit Converter 2026")
        # 1. Define available untis relative to meters
        self.units = {
            "Miles": 1609.34,
            "Kilometers": 1000.0,
            "Meters": 1.0,
            "Feet": 0.3048
        } 

        # 2. Create input label
        tk.Label(root, text = "Enter Value: ").pack(pady = (10, 0))
        self.input_val = tk.Entry(root)
        self.input_val.pack(pady=10)

        #3. Enter dropdown menu
        tk.Label(root, text="From:").pack()
        self.from_unit_cb = ttk.Combobox(root, values=list(self.units.keys()), state="readonly")
        self.from_unit_cb.set("Miles") # Default value
        self.from_unit_cb.pack(pady=5)

        tk.Label(root, text =  "To:").pack()
        self.to_unit_cb = ttk.Combobox(root, values=list(self.units.keys()), state="readonly")
        self.to_unit_cb.set("Kilometers") # Default value
        self.to_unit_cb.pack(pady=5)


        # 4. Create Conversion Button (Event Handling)
        self.calc_btn = tk.Button(root, text="Convert", command=self.calculate)
        self.calc_btn.pack(pady = 20)

        # 5. Create Result Label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
             # Get values from GUI
            value = float(self.input_val.get())
            from_unit = self.from_unit_cb.get()
            to_unit = self.to_unit_cb.get()

            # Logic: Convert input to METERS (base unit), then to target unit
            value_in_meters = value * self.units[from_unit]
            result = value_in_meters / self.units[to_unit]


            self.result_label.config(text = f"Result: {result:.2f} {to_unit}")

        except ValueError:
            self.result_label.config(text="Error: Enter a valid number")  
            
if __name__ == "__main__":
    root =  tk.Tk()
    app = UnitConverter(root)
    root.mainloop()
