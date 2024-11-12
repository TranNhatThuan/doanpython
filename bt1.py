import tkinter as tk
from tkinter import ttk
from tkinter import Menu, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x400")
        
        # Menu
        self.create_menu()
        
        # Tab
        self.create_tabs()
        
        # Danh sách lịch sử tính toán
        self.history = []
        
    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file) 
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)
        
    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)
        
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Calculator')
        self.create_calculator(tab1)
        
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Lịch sử tính toán')
        self.create_history_tab(tab2)
        
        tab_control.pack(expand=1, fill="both")
        
    def create_calculator(self, frame):
        label1 = tk.Label(frame, text="Số thứ nhất:", font=('Arial', 12), bg='#D3D3D3', fg='black')  # Chỉnh màu chữ thành đen
        label1.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.num1_entry = tk.Entry(frame, width=15, font=('Arial', 12), bg='#D3D3D3', fg='black')  # Màu chữ khi nhập
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)
        self.num1_entry.bind("<FocusIn>", self.on_focus_in)  # Đổi màu khi nhấp vào
        
        label2 = tk.Label(frame, text="Số thứ hai:", font=('Arial', 12), bg='#D3D3D3', fg='black')  # Chỉnh màu chữ thành đen
        label2.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.num2_entry = tk.Entry(frame, width=15, font=('Arial', 12), bg='#D3D3D3', fg='black')  # Màu chữ khi nhập
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)
        self.num2_entry.bind("<FocusIn>", self.on_focus_in)  # Đổi màu khi nhấp vào
        
        self.operation_var = tk.StringVar(value="+") 
        operations = ["+", "-", "*", "/"]
        self.operation_menu = tk.OptionMenu(frame, self.operation_var, *operations)
        self.operation_menu.config(bg='#D3D3D3', font=('Arial', 12), fg='black')  # Chỉnh màu chữ thành đen
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)
        
        calc_button = tk.Button(frame, text="Tính toán", command=self.calculate, font=('Arial', 12), bg='#4CAF50', fg='Blue')
        calc_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label = tk.Label(frame, text="Kết quả: ", font=('Arial', 12), bg='#D3D3D3', fg='black')  # Chỉnh màu chữ thành đen
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
        
    def create_history_tab(self, frame):
        history_label = tk.Label(frame, text='Lịch sử tính toán', font=('Arial', 14), bg='#D3D3D3', fg='black')  # Chỉnh màu chữ thành đen
        history_label.pack(pady=10)
        
        self.history_listbox = tk.Listbox(frame, width=50, height=10, font=('Arial', 12), bg='#D3D3D3')
        self.history_listbox.pack(pady=10)
        
        clear_history_button = tk.Button(frame, text="Xóa lịch sử", font=('Arial', 12), command=self.clear_history)
        clear_history_button.pack(pady=10)
    
    def on_focus_in(self, event):
        event.widget.config(fg='black')  # Đặt màu chữ khi nhấp vào là đen
    
    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                raise ValueError("Phép toán không hợp lệ!")
            
            self.result_label.config(text=f"Kết quả: {result}")
            self.history.append(f"{num1} {operation} {num2} = {result}")
            self.update_history()
        
        except ValueError as ve:
            messagebox.showerror("Error", f"Lỗi nhập liệu: {ve}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Không thể chia cho 0!")
            
    def update_history(self):
        self.history_listbox.delete(0, tk.END)
        for entry in self.history:
            self.history_listbox.insert(tk.END, entry)
            
    def clear_history(self):
        self.history.clear()
        self.update_history()
    
    def new_file(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.operation_var.set("+") 
        self.result_label.config(text="Kết quả: ")
        
    def about(self):
        messagebox.showinfo("About", "TranNhatThuan - 2274802010865")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()