from typing import Any

from pydantic import BaseModel


class PreprocessRequest(BaseModel):
    city: str