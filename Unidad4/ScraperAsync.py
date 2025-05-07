import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def obtener_titulo(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(f"Obteniendo título de {url}")
            titulo = soup.find('title').text
            print(f"Título obtenido: {titulo}")
    
async def main():
    urls = [
        'https://www.python.org',
        'https://www.wikipedia.org',
        'https://www.github.com'
    ]
    
    tareas = [obtener_titulo(url) for url in urls]
    await asyncio.gather(*tareas)

asyncio.run(main())