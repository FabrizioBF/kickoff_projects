from tkinter import Label, Tk
import time

# Configuração da janela principal
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("500x200")  # Ajustado para acomodar o texto
app_window.resizable(1, 1)

# Configuração do estilo
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"  # Amarelo claro
foreground = "#363529"  # Cinza escuro
border_width = 25

# Configuração do rótulo para o relógio
label = Label(
    app_window, font=text_font, bg=background, fg=foreground, bd=border_width
)
label.grid(row=0, column=1)

# Função para atualizar o relógio


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(1000, digital_clock)  # Atualização a cada segundo


# Inicializa o relógio digital
digital_clock()

# Executa o loop principal da interface
app_window.mainloop()
