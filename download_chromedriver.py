import os
import shutil
import zipfile

import requests

if not os.path.isfile("chromedriver.exe"):
    print("chromedriver.exe가 존재하지 않습니다. 최신 릴리즈를 최초 1회 다운로드합니다.")

    chromedriver_latest_release = requests.get(
        "https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text.strip()

    r = requests.get("https://chromedriver.storage.googleapis.com/"
                     + chromedriver_latest_release + "/chromedriver_win32.zip", stream=True)

    with open("chromedriver_win32.zip", "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

    with zipfile.ZipFile("chromedriver_win32.zip") as zip:
        zip.extract("chromedriver.exe")

    os.remove("chromedriver_win32.zip")
