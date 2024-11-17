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
    > String filter
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
    """
    def cl_replace(self, old, new, count=-1):
        if not old or len(old) > len(self.string):
            raise ValueError("Chuỗi cần thay không hợp lệ!")
        
        if old == new or count == 0:
            return self.string

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
    """ Kỹ thuật:
    > None cho tham số
    > Slicing
    """
    def cl_find(self, s, start=0, end=None):
        if not s:
            raise ValueError("Chuỗi con không hợp lệ!")
        
        if end is None:
            end = len(self.string)
        
        for i in range(start, end - len(s) + 1):
            if self.string[i:i + len(s)] == s:
                return i
        return -1
    



    # Clone lại phương thức isspace() của lớp str:
    """ Kỹ thuật:
    > String filter
    """
    def cl_isspace(self):
        if not self.string:
            return False

        whitespaces = ' \t\n\r\x0b\x0c'
        for char in self.string:
            if char not in whitespaces:
                return False
        return True

    
    # Clone lại phương thức split() của lớp str
    """ Kỹ thuật:

    """
    def cl_split(self, sep=None, count=-1):
        if sep is None:
            sep = ' \t\n\r\x0b\x0c'
        
        result = []
        lc = 0
        for i in range(0, len(self.string)):
            if self.string[i] in sep:
                result.append(self.string[lc:i])
                lc = i + 1
        result.append(self.string[lc:])
        return result

        

# Main function
if __name__ == '__main__':
    s = cl_Str('Hello World')
    # s = cl_Str('-')
    print(s.cl_split('l '))
    exit(0)