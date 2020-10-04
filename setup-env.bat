@Echo Off
REM setup environment variable in Python
echo ********* Creating and Setting up virtual environment *********
py -m venv env

echo Virtual Environment created successfylly
call .\env\Scripts\activate

call pip list

call py -m pip install --upgrade pip

echo PIP upgraded successfylly

echo Installing dependencies

call pip install -r requirements.txt

cd .
REM pause

