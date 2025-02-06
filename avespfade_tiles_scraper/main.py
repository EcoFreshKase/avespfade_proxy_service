import aiohttp
import asyncio
import os

async def download_image(session, url, file_path):
    async with session.get(url) as response:
        if response.status == 200:
            with open(file_path, 'wb') as file:
                file.write(await response.read())
            print(f"Image successfully downloaded: {file_path}")
        else:
            print(f"Failed to retrieve image ({file_path}). Status code: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(30):
            for j in range(30):
                for k in range(30):
                    image_url = f'https://www.avespfade.de/tiles/{i}/{j}/{k}.png'
                    save_path = f'./images/tile_{i}_{j}_{k}.png'

                    if os.path.exists(save_path):
                        print(f"Image already exists: {save_path}")
                        continue
                    
                    tasks.append(download_image(session, image_url, save_path))

        await asyncio.gather(*tasks)

asyncio.run(main())