import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x200")
        self.title("Temperature Converter")
        
        # Creating 2 columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        
        self.left = ctk.CTkFrame(self)
        self.right = ctk.CTkFrame(self)
        
        self.left.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.right.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Adding content for the left column
        self.left.grid_columnconfigure(0, weight=1)
        
        self.in_label = ctk.CTkLabel(self.left, text='Input temperature') # anchor='center', bg_color='#3e66e0', corner_radius=300
        self.in_label.grid(row=0, column=0, sticky='n', padx=12, pady=(12, 6))
        
        self.in_entry = ctk.CTkEntry(self.left, placeholder_text="Enter value")
        self.in_entry.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 8))

        # Temperature dropdown on the left
        self.unit_in_var = ctk.StringVar(value="°C")
        self.unit_in = ctk.CTkOptionMenu(self.left, values=["°C", "°F", "K"],
                                        variable=self.unit_in_var)
        self.unit_in.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))

        # Adding content for the right column
        self.right.grid_columnconfigure(0, weight=1)
        self.out_label = ctk.CTkLabel(self.right, text='Output temperature')
        self.out_label.grid(row=0, column=0, sticky="n", padx=12, pady=(12, 6))
        
        self.output_var = ctk.StringVar(value='')
        self.output_field = ctk.CTkEntry(self.right, textvariable=self.output_var,
                                         state='disabled', takefocus=0, justify='right')
        self.output_field.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 8))
        
        # Temperature dropdown on the right
        self.unit_out_var = ctk.StringVar(value="°F")
        self.unit_out = ctk.CTkOptionMenu(self.right, values=["°C", "°F", "K"],
                                  variable=self.unit_out_var)
        self.unit_out.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 12))
        
        self.convert_btn = ctk.CTkButton(self.left, text="Convert", command=self.on_convert)
        self.convert_btn.grid(row=3, column=0, padx=12, pady=(4, 12), sticky="e")

    def on_convert(self, event=None):
        try:
            x = float(self.in_entry.get())
            k = self.to_kelvin(x, self.unit_in_var.get())
            y = self.from_kelvin(k, self.unit_out_var.get())
            self.output_var.set(f"{y:.2f} {self.unit_out_var.get()}")
        except ValueError:
            self.output_var.set("Invalid number")
    
    def to_kelvin(self, x, u):
        if u == "°C": return x + 273.15
        if u == "°F": return (x - 32) * 5/9 + 273.15
        return x  # K

    def from_kelvin(self, k, u):
        if u == "°C": return k - 273.15
        if u == "°F": return (k - 273.15) * 9/5 + 32
        return k  # K

    def on_convert(self):
        try:
            x = float(self.in_entry.get())
            k = self.to_kelvin(x, self.unit_in_var.get())
            y = self.from_kelvin(k, self.unit_out_var.get())
            self.output_var.set(f"{y:.2f} {self.unit_out_var.get()}")
        except ValueError:
            self.output_var.set("Invalid number")


        # Write to the read-only textbox
        self.output_field.configure(state="normal")
        self.output_field.delete("1.0", "end")
        self.output_field.insert("1.0", msg)
        self.output_field.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()
