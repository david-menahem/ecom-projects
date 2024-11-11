from pydantic import BaseModel


class Track(BaseModel):
    track_name: str
    playcount: str
    track_url: str

