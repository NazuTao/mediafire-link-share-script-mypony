import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar las dependencias: {e}")
        sys.exit(1)

# Instalar las dependencias al inicio del script
install_dependencies()

# Importar las dependencias necesarias después de haberlas instalado
import customtkinter as ctk

# Función para reemplazar comas y una URL específica con otra URL
def replace_text():
    input_text = text_entry.get("1.0", "end-1c")  # Obtener el texto del widget de entrada
    output_text = input_text.replace(",", " http://mediafire.com/?")
    output_text = output_text.replace("https://www.mediafire.com/folder/", " http://mediafire.com/?")
    text_output.delete("1.0", "end")  # Limpiar el widget de salida
    text_output.insert("1.0", output_text)  # Insertar el texto modificado en el widget de salida

# Crear la ventana principal
root = ctk.CTk()
root.title("Convertir")
root.geometry("600x400")

# Crear widgets
text_entry = ctk.CTkTextbox(root, height=10, width=50)
text_output = ctk.CTkTextbox(root, height=10, width=50)
replace_button = ctk.CTkButton(root, text="Convertir", command=replace_text)

# Colocar widgets en la ventana
text_entry.pack(pady=10, padx=10, expand=True, fill='both')
replace_button.pack(pady=5)
text_output.pack(pady=10, padx=10, expand=True, fill='both')

# Ejecutar la aplicación
root.mainloop()
