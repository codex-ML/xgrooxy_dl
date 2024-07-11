import asyncio
from backup.search import scrape_videos
from backup.download import download_video

# async def lol():
#     videos_json = await scrape_videos("cosplay")
#     print(videos_json)

# # Run the async function using asyncio.run
# asyncio.run(lol())

async def dl():
    videos_json = await download_video("https://xgroovy.com/videos/265052/cosplay-wonder-woman-sucks-dildo-and-gets-her-pussy-rammed/")
    print(videos_json)

# Run the async function using asyncio.run
asyncio.run(dl())
