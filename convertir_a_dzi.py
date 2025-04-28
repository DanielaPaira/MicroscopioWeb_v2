import pyvips
import os
import json

# Carpeta donde están las imágenes
input_directory = "."

# Convertir todas las .tif a .dzi
for filename in os.listdir(input_directory):
    if filename.endswith(".tif"):
        name = filename.rsplit('.', 1)[0]
        input_path = os.path.join(input_directory, filename)
        output_prefix = os.path.join(input_directory, name + "_dzi")

        print(f"🔍 Convirtiendo {filename}...")
        image = pyvips.Image.new_from_file(input_path, access="sequential")
        image.dzsave(output_prefix)
        print(f"✅ ¡Conversión completada para {filename}!")

# Crear imagenes.json con la lista de archivos .dzi
dzi_files = [f for f in os.listdir(input_directory) if f.endswith(".dzi")]

with open("imagenes.json", "w") as f:
    json.dump(dzi_files, f)

print("📝 Archivo imagenes.json generado con éxito:")
print(dzi_files)
