call create_package.bat
pip install virtualenv
virtualenv venv --system-site-packages
call .\venv\Scripts\activate.bat
pip install .