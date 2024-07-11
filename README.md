
```
python setup.py sdist bdist_wheel
```


```
pip install .
```

#USAGE
```
import asyncio
from xgroovy import scrape_videos, download_video

async def test_scrape_videos():
    videos = await scrape_videos("cosplay")
    assert len(videos) > 0

async def test_download_video():
    video_url = await download_video("your_video_page_url_here")
    assert video_url is not None

if __name__ == "__main__":
    asyncio.run(test_scrape_videos())
    asyncio.run(test_download_video())

```
