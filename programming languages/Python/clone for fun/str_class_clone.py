class cl_str:
    def __init__(self, init_str=''):
        self.string = init_str
    
    # Clone lại phương thức upper() của lớp str
    def cl_upper(self):
        result = []
        for char in self.string:
            if 'a' <= char <= 'z':
                result.append(chr(ord(char) - 32))
            else:
                result.append(char)
        return ''.join(result)


# Main function
if __name__ == '__main__':
    s = cl_str('Hello World!')
    print(s.cl_upper())
    exit(0)