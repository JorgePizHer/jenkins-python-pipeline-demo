import argparse

def process_file(file_path):
    try:
        with open(file_path, "r") as f:
            data = f.read()
        return f"Contenido del archivo:\n{data}"
    except:
        return "No se pudo leer el archivo."

parser = argparse.ArgumentParser()
parser.add_argument("--msg", type=str, required=True)
parser.add_argument("--file", type=str, required=False)

args = parser.parse_args()

print(f"Mensaje recibido: {args.msg}")

if args.file:
    print(process_file(args.file))
else:
    print("No se proporcionó archivo de entrada.")
