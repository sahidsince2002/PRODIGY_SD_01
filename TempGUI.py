import tkinter as tk 

bg_color = "white"
radio_fg_color = "Blue"
result_color = " Black"

def convert():
    temp=float(textbox.get())
    
    if var.get()==1:
         farh = (1.8 * temp) + 32 
         kel = temp + 273.15
         result1.config(text=f"{farh:.2f} def F")
         result2.config(text=f"{kel:.2f} def K")
         
         
    if var.get()==2: 
         cel = (temp - 32) * 0.55
         kel = ((temp -32) * 0.55) + 273.15  
         result1.config(text=f"{cel:.2f} def C")
         result2.config(text=f"{kel:.2f} def K")
    
    if var.get()==3: 
          cel = (temp - 273.15)
          farh = ((temp -273.15) * 1.8) + 32 
          result1.config(text=f"{cel:.2f} def C")
          result2.config(text=f"{farh:.2f} def F")     
         
    

    
    
    

root = tk.Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Temperature Calculator")

label = tk.Label(root, text="Temperature Converter ", font=("Times New Roman",18))
label.pack(pady=10)
entry_label= tk.Label(root, text="Enter the temperature ", font=("Times New Roman", 15,'bold'))
entry_label.pack()


textbox = tk.Entry(root, font=("Times New Roman",16))
textbox.pack(pady=10)

var=tk.IntVar()
#creating a frame 

frame = tk.Frame(root)
frame.pack(pady=10)




first = tk.Radiobutton(frame, text="Celcius to Frahenheit and Kelvin", variable=var, value=1, font=("Arial",14),
                       bg=bg_color, activebackground=bg_color, activeforeground=radio_fg_color)
first.grid(row=0, column=0)

second = tk.Radiobutton(frame, text="Frahenheit to Celcius and Kelvin", variable=var, value=2, font=("Arial",14),
                       bg=bg_color, activebackground=bg_color, activeforeground=radio_fg_color)
second.grid(row=1, column=0)

third = tk.Radiobutton(frame, text="Kelvin to Celcius and Frahenheit", variable=var, value=3, font=("Arial",14),
                       bg=bg_color, activebackground=bg_color, activeforeground=radio_fg_color)
third.grid(row=2, column=0)




button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert)
button.pack()

result1 = tk.Label(root, text="", font=("Times New Roman",12))
result1.pack(pady=10)

result2 = tk.Label(root, text="", font=("Times New Roman",12))
result2.pack(pady=10)



root.mainloop()