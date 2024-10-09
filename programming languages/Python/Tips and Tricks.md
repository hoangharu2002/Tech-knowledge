# There are a lot of tips and tricks for "Pythonista"

## Optimize script

1. Turn off unwanted warning in python (I mostly use while plotting)

``` Python
import warnings
warnings.filterwarnings("ignore")
```

2. "if __name__ == '__main__':" for discard unwanted running-code when importing a file

3. 