

MONGODB_URL = os.getenv("MONGODB_URL")

#Inicializar el cliente de  MongoDB
client = AsyncIOMotorClient(MONGODB_URL)

#seleccionar la base de datos(Se creara automaticamente si no existe)

database = client.ambiente502

#Seleccion la conexion se creara automaticante si no existe

collection = database.mesas

#Funcion para probar la conexion a la base de datos 
async def test_connection():
    try:
        await client.admin.command("ping")
        print("Conexion a MongoDB exitosa")
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_connection())  

# 