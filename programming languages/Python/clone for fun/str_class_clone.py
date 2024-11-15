from io import StringIO

class cl_Str:

    # Phương thức khởi tạo
    def __init__(self, str_input):
        self.string = str_input

    # Clone lại phương thức join() của lóp str
    """ Kỹ thuật:
    > StringIO
    > (Có thể) List thay String
    > Cờ hiệu 1 lần
    """
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
    """ Kỹ thuật:
    > List thay String
    """
    def cl_upper(self):
        result = []
        for char in self.string:
            if 'a' <= char <= 'z':
                result.append(chr(ord(char) - 32))
            else:
                result.append(char)
        return ''.join(result)
    
    # Clone lại phương thức lower() của lớp str
    """ Kỹ thuật:
    > List thay String
    """
    def cl_lower(self):
        result = []
        for char in self.string:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char) 
        return ''.join(result)
    
    # Clone lại phương thức strip() của lớp str
    """ Kỹ thuật:
    > None cho tham số
    > Sử dụng string để lưu giá trị lọc
    > Hai vòng lặp
    """
    def cl_strip(self, chars=None):
        if chars is None:
            chars = ' \t\n\r\x0b\x0c'   # gán cho chars tất cả các kí tự khoảng trắng
        
        # Ý tưởng: tìm phần không bị cắt

        start = 0
        # tìm vị trí đầu của phần không cắt
        while start < len(self.string) and self.string[start] in chars:
            start += 1

        end = len(self.string) - 1
        # tìm vị trí cuối của phần không cắt
        while end > start and self.string[end] in chars:
            end -= 1
        
        return self.string[start:end + 1]
    
    # Clone lại phương thức replace() của lớp str
    """ Kỹ thuật:
    > List thay String
    > Slicing
    > Tìm chuỗi con
    """
    def cl_replace(self, old, new, count=-1):
        if old == '':
            print("Không có chuỗi rồi sao mà tìm?")
            return 1
        result = []
        index = 0
        while index < len(self.string):
            if self.string[index:index + len(old)] == old and count != 0:
                result.append(new)
                count -= 1
                index += len(old)
            else:
                result.append(self.string[index])
                index += 1
        return ''.join(result)
    
    # Clone lại phương thức find() của lớp str
    """ Kỹ thuật"
    > None cho tham số
    > Slicing
    """
    def cl_find(self, s, start=0, end=None):
        if end is None:
            end = len(self.string)

        for i in range(start, end):
            if self.string[i:i + len(s)] == s:
                return start
            else:
                start += 1
        return -1
    
    # Clone lại phương thức split() của lớp str
    """ Kỹ thuật:

    """
    def cl_split(self, sep=None, count=-1):
        if sep is None:
            sep = ' \t\n\r\x0b\x0c'
        result = []
        start = 0
        end = 0
        while end < len(self.string):
            if self.string[end:end + len(sep)] == sep:
                result.append(self.string[start:end])
                end += len(sep)
                start = end
            else:
                pass

        

# Main function
if __name__ == '__main__':
    s = cl_Str('Hello World')
    # s = cl_Str('-')
    print(s.cl_find('l'))
    exit(0)