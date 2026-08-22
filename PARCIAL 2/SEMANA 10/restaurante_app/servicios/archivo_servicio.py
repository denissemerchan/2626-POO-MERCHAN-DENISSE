import json
import os
from typing import List
from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json") -> None:
        self.ruta_archivo = ruta_archivo

    def cargar_productos(self) -> List[Producto]:
        productos: List[Producto] = []
        if not os.path.exists(self.ruta_archivo):
            return productos

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if isinstance(datos, list):
                    for registro in datos:
                        try:
                            prod = Producto(
                                id_producto=registro["id_producto"],
                                nombre=registro["nombre"],
                                precio=registro["precio"]
                            )
                            productos.append(prod)
                        except (KeyError, ValueError) as error:
                            print(f"[Advertencia] Registro omitido: {error}")
        except FileNotFoundError:
            print("[Info] El archivo no existe. Se iniciará con lista vacía.")
        except json.JSONDecodeError:
            print("[Error] El archivo JSON tiene un formato inválido. Se iniciará con lista vacía.")
        except PermissionError:
            print("[Error] Permisos insuficientes para leer el archivo JSON.")

        return productos

    def guardar_productos(self, productos: List[Producto]) -> bool:
        try:
            directorio = os.path.dirname(self.ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            lista_diccionarios = [p.a_diccionario() for p in productos]

            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("[Error] Permisos insuficientes para escribir en el archivo JSON.")
            return False
        except Exception as error:
            print(f"[Error inesperado al guardar]: {error}")
            return False