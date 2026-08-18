import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")
if MONGODB_URL:
    MONGODB_URL = MONGODB_URL.strip()

MONGODB_DB = os.getenv("MONGODB_DB", "ambiente502").strip()

# Inicializar el cliente de MongoDB
client = AsyncIOMotorClient(MONGODB_URL)

# Seleccionar la base de datos (se creará automáticamente si no existe)
database = client[MONGODB_DB]

#Seleccion la conexion se creara automaticante si no existe

collection = database.mesas

#Funcion para probar la conexion a la base de datos 
async def test_connection():
    try:
        await client.admin.command("ping")
        print("Conexion a MongoDB exitosa")
        #2. crear un documento de prueba
        doctest = {
            "nombre":"Matias Arenas",
            "Edad":"17",
            "genero": "Masculino"
    
        }
        # 3. Guardar el documento en la coleccion
        print("Guardando documento de prueba en la coleccion....")
        result = await collection.insert_one(doctest)
        print(f"Documento insertado con el ID: {result.inserted_id}")



        # 4. BUscar el dato guardado en la coleccion
        datarequest = await collection.find_one({"_id":result.inserted_id})
        print("documento encontrado: {datarequest}")
        

        # 5. Actualizar el documento guardado
        






    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())  


