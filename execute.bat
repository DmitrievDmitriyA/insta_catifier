set USER=%1
set USER_PATH="insta_sources\%~1"

call .\venv\Scripts\activate.bat
instagram-scraper %USER% -d %USER_PATH%
python add_cats.py %USER%