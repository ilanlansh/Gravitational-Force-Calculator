import tkinter as tk;

##G = 6.67408 * (10 ** (-11));
##M = 5.972 * (10 ** 24);  #kg
##m = 7.34767309 * (10*22);  #kg
##r = 384400000;  #m
##
##F = (G * M * m) / (r ** 2);

G = 6.67408 * (10 ** (-11));  # gravitational constant
root = tk.Tk();
root.title("Gravitational Force Calculator");

def calculate(gc, M, m, r):
    F = (gc * M * m) / (r ** 2);
    return F;

def show():
    F = calculate(
        G,
        float(eval(entries[0].get())),
        float(eval(entries[1].get())),
        float(eval(entries[2].get()))
    );
    ans['text'] = f"F = {F}"
    
    
heading = tk.Label(root, text = 'gravitational force calculator', font = 'courier 16 bold')
heading.grid(row = 0, column = 1);

for label in (labels1 := [
    tk.Label(root, text = ' M = ', font = 'courier 12 bold', height = 2, ),
    tk.Label(root, text = ' m = ', font = 'courier 12 bold', height = 2, ) ,
    tk.Label(root, text = ' r = ', font = 'courier 12 bold', height = 2, ),
]):
    label.grid(row = labels1.index(label) + 1, column = 0);

for entry in (entries := [
    tk.Entry(root, font = 'courier 20 bold', fg = '#0d54a1', ),  # M
    tk.Entry(root, font = 'courier 20 bold', fg = '#0d54a1', ),  # m
    tk.Entry(root, font = 'courier 20 bold', fg = '#0d54a1', ),  # r
]):
    entry.grid(row = entries.index(entry) + 1, column = 1);

for label in (labels2 := [
    tk.Label(root, text = 'kg ', font = 'courier 12 bold', ),
    tk.Label(root, text = 'kg ', font = 'courier 12 bold', ),
    tk.Label(root, text = 'm ', font = 'courier 12 bold', ),
]):
    label.grid(row = labels2.index(label) + 1, column = 2);

button = tk.Button(root, text = 'calculate', command = show, font = 'courier 16 bold');
button.grid(row = 4, column = 1);

ans = tk.Label(root, text = 'F = ', font = 'courier 16 bold')
ans.grid(row = 5, column = 1);

root.mainloop();
