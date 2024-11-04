class cl_str:

    # Phương thức khởi tạo
    def __init__(self, str_input):
        self.string = str_input
    # Clone lại phương thức upper() của lớp str
    def cl_upper(self):
        result = []
        for char in self.string:
            if 'a' <= char <= 'z':
                result.append(chr(ord(char) - 32))
            else:
                result.append(char)
        return ''.join(result)
    # Clone lại phương thức lower() của lớp str
    def cl_lower(self):
        result = []
        for char in self.string:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)

# Main function
if __name__ == '__main__':
    s = cl_str('Hello World!')
    print(s.cl_lower())
    exit(0)