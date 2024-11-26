from io import StringIO
import unicodedata

class cl_Str:


    # Phương thức khởi tạo
    def __init__(self, str_input):
        self.string = str_input




    # Clone lại phương thức join() của lóp str
    """ Techiniques:
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
    """ Techiniques:
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
    



    # Clone lại phương thức isupper() của lớp str
    """ Techiniques:
    > Generator Expression
    """
    def cl_isupper(self):
        if not self.string:
            return False

        return all('A' <= char <= 'Z' for char in self.string)



    
    # Clone lại phương thức lower() của lớp str
    """ Techiniques:
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
    """ Techiniques:
    > None cho tham số
    > Sử dụng string để lưu giá trị lọc
    > Filter
    """
    def cl_strip(self, chars=None):
        if chars is None:
            chars = {' ', '\t', '\n', '\r', '\x0b', '\x0c'}

        if chars:
            return self.string

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
    """ Techiniques:
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
    """ Techiniques:
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
    """ Techiniques:
    > Filter
    > Generator Expression
    """
    def cl_isspace(self):
        if not self.string:
            return False

        whitespaces = {' ', '\t', '\n', '\r', '\x0b', '\x0c'}
        return all(char in whitespaces for char in self.string)




    # Clone lại phương thức split() của lớp str
    """ Techiniques:
    > buffer
    > slicing
    """
    def cl_split(self, sep=None, count=-1):
        result = []
        buffer = []

        if sep is None:
            for char in self.string:
                if char.isspace():
                    result.append(''.join(buffer))
                    buffer = []
                else:
                    buffer.append(char)
            if buffer:
                result.append(''.join(buffer))
        else:
            sep_len = len(sep)
            string_len = len(self.string)
            i = 0

            while i < string_len:
                if self.string[i:i + sep_len] == sep:
                    result.append(''.join(buffer))
                    buffer = []
                    i += sep_len
                else:
                    buffer.append(self.string[i])
                    i += 1
            if buffer:
                result.append(''.join(buffer))

        return result
    



    # Clone lại phương thức isalpha() của lớp str
    """ Techniques:
    > Generator Expression
    """
    def cl_isalpha(self):
        if not self.string:
            return False
        
        return all(unicodedata.category(char).startswith("L") for char in self.string)




# Main function
if __name__ == '__main__':
    s = cl_Str('Γειάσου')
    # s = cl_Str('-')
    print(s.cl_isalpha())
    exit(0)