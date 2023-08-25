import tkinter as tk

# Create the main window
window = tk.Tk()
window.title('Calculator')

# Create the display
display = tk.Entry(window, width=20)
display.grid(row=0, column=0, columnspan=4)

# Function to handle button clicks

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

# Create the number buttons
for i in range(9):
    button = tk.Button(window, text=str(i+1), command=lambda i=i: button_click(i+1))
    button.grid(row=(i+2)//4, column=(i+2)%4)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, command=lambda operator=operator: button_click(operator))
    button.grid(row=i+2, column=i%4)

# Create the equal button
equal_button = tk.Button(window, text='=', command=lambda: button_click('='))
equal_button.grid(row=5, column=2)

# Run the main loop
window.mainloop()