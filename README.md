# Notable-Take-Home

## Setup

The project uses pipenv as a python package manager. Essentially, it's pip and venv combined, once you're in pipenv's virtual environment, just treat pipenv as you would pip commands. For more information see here: https://realpython.com/pipenv-guide/

Install pipenv (or with homebrew for mac)

```
pip3 install pipenv
```

Create and enter pipenv virtual environment

```
pipenv shell
```

Install Pipfile.lock
```
pipenv install
```

Run the code test file

```
python test.py
```

Exit virtual environment
```
exit
```


## Assumptions and code design explanations

I implemented the transformation based on the following assumptions:
- If the first number the parser encounters is not equal to 1, it creates empty list entries until it reaches the encountered number.
- If the first number is not between 1 and 9, an error is raised.
- If the note is not present in the input, the user is asked to enter it manually
- If the "number next" phrase is encountered before the list is started, the parser treats it as ordinary text.
- The information between the "Number [n]" phrase and the "Number [n+1]" phrase is a part of the "Number [n]" list item no matter the length.

There are obviously some trade-offs with my decisions but I believe that the code is flexible enough to be adjusted in case of clarifications or additional requirements.

## Potential improvements:
- Raise an error if the same number is encountered (or automatically self-correct to the closest available number?)
- Produce a cutoff and transition to the next list item if the item length exceed x characters.
