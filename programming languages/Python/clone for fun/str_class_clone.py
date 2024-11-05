from io import StringIO

class cl_Str:

    # Phương thức khởi tạo
    def __init__(self, str_input):
        self.string = str_input

    # Clone lại phương thức join() của lóp str
    def cl_join(self, iterator):
        result = StringIO()
        first = True
        for item in iterator:
            if first:
                first = False
            else:
                result.write(self.string)
            result.write(item)
        return result.getvalue()

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
    
    # Clone lại phương thức strip() của lớp str
    def cl_strip(self, chars=None):
        if chars is None:
            chars = ' \t\n\r\x0b\x0c'   # gán cho chars tất cả các kí tự khoảng trắng
        
        start = 0
        # tìm vị trí đầu của phần không cắt
        while start < len(self.string) and self.string[start] in chars:
            start += 1

        end = len(self.string) - 1
        # tìm vị trí cuối của phần không cắt
        while end > start and self.string[end] in chars:
            end -= 1
        
        return self.string[start:end + 1]

# Main function
if __name__ == '__main__':
    s = cl_Str('  Hello  World!  ')
    # s = cl_Str('-')
    print(s.cl_strip())
    exit(0)