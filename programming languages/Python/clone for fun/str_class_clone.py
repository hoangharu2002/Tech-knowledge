class cl_str:
    def __init__(self, init_str=''):
        self.string = init_str
    
    # Clone lại phương thức upper() của lớp str
    def upper(self):
        result = ""
        for char in self.string:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        return result


# Main function
if __name__ == '__main__':
    s = cl_str('Hello World!')
    print(s.upper())
    exit(0)