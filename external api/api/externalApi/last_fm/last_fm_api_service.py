from typing import List

import httpx

from api.externalApi.last_fm.model.Track import Track
from config.config import Config

config = Config()


async def get_top_tracks_by_artist(artist: str) ->List[Track]:
    url = (f"{config.LAST_FM_BASE_URL}?method=artist.gettoptracks"
           f"&artist={artist}&api_key={config.LAST_FM_API_KEY}&format=json")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            tracks = [Track(
                track_name=track['name'],
                playcount=track['playcount'],
                track_url=track['url']
            )
                for track in data['toptracks']['track']]

            return tracks

        except httpx.HTTPStatusError as exception:
            print(f"Cannot fetch artist: {artist} top tracks: {exception.response}")
            return []



