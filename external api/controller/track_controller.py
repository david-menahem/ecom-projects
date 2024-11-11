from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from api.externalApi.last_fm import last_fm_api_service
from api.externalApi.last_fm.model.Track import Track

router = APIRouter(
    prefix="/artist_top_tracks",
    tags=["artist_top_tracks"]
)


@router.get(path="/{artist}", status_code=status.HTTP_200_OK)
async def get_top_tracks_by_artist(artist: str) -> List[Track]:
    try:
        return await last_fm_api_service.get_top_tracks_by_artist(artist)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))