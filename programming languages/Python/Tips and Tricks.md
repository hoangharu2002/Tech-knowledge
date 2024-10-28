# There are a lot of tips and tricks for "Pythonista"

## Optimize runtime

1. Turn off unwanted warning in python (I mostly use while plotting)

``` Python
import warnings
warnings.filterwarnings("ignore")
```

2."if __name__ == '__main__':" for discard unwanted running-code when importing a file

## Command Promt

1. python -s [filename] : run python file without module `site`

2. python --version : kiểm tra phiên bản python interpreter đang dùng

3. python -m [filename] : thực thi file theo dạng modules

## Scripting

1. `sys.version` : trả về phiên bản python hiện tại

2. `a = b = c = 1` : gán một giá trị cho nhiều biến

3. `a, b, c = 1, 2, 3` : gán nhiều giá trị cho nhiều biến

4. `a = 1,` : tạo một tuple với 1 phần tử

5. use `in` to check if a string in a bigger string (ex: 'str' in 'string')


## Tips

