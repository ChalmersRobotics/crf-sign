On windows:

```
python3 -m venv crfsign

crfsign\Scripts\activate.bat

pipenv sync

pipenv run python crfsign.py
```

On linux (maybe?):

```
python3 -m venv crfsign

source crfsign/bin/activate

pipenv sync

pipenv run python crfsign.py
```