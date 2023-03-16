from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


RECITATION_HOURS = {"a": "09:00~09:50", "b": "10:00~10:50",
                    "c": "11:00~11:50", "d": "12:00~12:50"}


@app.get("/section_info/{section_id}")
def get_section_info(section_id: str):

    if section_id is None:
        raise HTTPException(status_code=404, detail="Missing section id")

    section_id = section_id.lower()

    # TODO

    if section_id == "a":
        return {
            "section": "section_name",
            "start_time": "HH:MM",
            "end_time": "HH:MM",
            "ta": ["taName1", "taName2"]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid section id")
