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
    > Generator Expression
    > Tenary Operator
    """
    def cl_upper(self):
        return ''.join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in self.string)
    



    # Clone lại phương thức isupper() của lớp str
    """ Techiniques:
    > Generator Expression
    """
    def cl_isupper(self):
        if not self.string:
            return False

        return all(unicodedata.category(char) == 'Lu' for char in self.string)




    # Clone lại phương thức islower() của lớp str
    """ Techniques:
    > Generator Expression
    """
    def cl_islower(self):
        if not self.string:
            return False
        
        return all(unicodedata.category(char) == 'Ll' for char in self.string)


    

    # Clone lại phương thức lower() của lớp str
    """ Techiniques:
    > List thay String
    """
    def cl_lower(self):
        return ''.join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in self.string)
    


    
    # Clone lại phương thức strip() của lớp str
    """ Techiniques:
    > Giá trị mặc nhiên None
    > Slicing
    > Filter với in
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
    



    # Clone lại phương thức lstrip() của lớp str
    """ Techniques:
    > Giá trị mặc nhiên None
    > Slicing
    > Filter với in
    """
    def cl_lstrip(self, chars=None):
        if chars is None:
            chars = {' ', '\t', '\n', '\r', '\x0b', '\x0c'}

        if not chars:
            return self.string
        
        start = 0
        while start < len(self.string) and self.string[start] in chars:
            start += 1

        return self.string[start:]
    



    # Clone lại phương thức rstrip() của lớp str
    """ Techniques:
    > Slicing
    > Giá trị mặc nhiên None
    > Filter với in
    """
    def cl_rstrip(self, chars=None):
        if chars is None:
            chars = {' ', '\t', '\n', '\r', '\x0b', '\x0c'}
        
        if not chars:
            return self.string
        
        end = len(self.string) - 1
        while end > -1 and self.string[end] in chars:
            end -= 1

        return self.string[0:end + 1]




    # Clone lại phương thức replace() của lớp str
    """ Techiniques:
    > List thay String
    > Slicing
    """
    def cl_replace(self, old, new, count=-1, /):
        if old == new or count == 0:
            return self.string
        
        if not old:
            return new + new.join(self.string) + new if self.string else new

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
        # Kiểm tra substring có tồn tại không
        if not s:
            raise ValueError("Chuỗi con không hợp lệ!")
        
        # Kiểm tra và cài đặt giá trị mặc định cho `end`
        if end is None:
            end = len(self.string)

        # Xử lý nếu `start` và `end` là số âm
        start = max(0, len(self.string) + start) if start < 0 else start
        end = max(0, len(self.string) + end) if start < 0 else end
        
        for i in range(start, end - len(s) + 1):
            if self.string[i:i + len(s)] == s:
                return i
        return -1
    



    # Clone lại phương thức rfind() của lớp str
    """ Techiniques
    > Slicing
    > Ternary Operator
    """
    def cl_rfind(self, s, start=0, end=None):
        # Kiểm tra chuỗi cần tìm có tồn tại không
        if s is None:
            raise ValueError("Chuỗi cần tìm không hợp lệ!")
        
        # Kiểm tra và cài đặt giá trị mặc định cho `end`
        if end is None:
            end = len(self.string)

        # Xử lý nếu `start`` và `end`` là số âm
        start = max(0, len(self.string) + start) if start < 0 else start
        end = max(0, len(self.string) + end) if start < 0 else end

        # Kiểm tra nếu chuỗi cần tìm rỗng
        if not s:
            return end

        # Lặp qua từng vị trí để tìm chuỗi
        for i in range(end - len(s), start - 1, -1):
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
    > Giá trị mặc nhiên None
    """
    def cl_split(self, sep=None, maxsplit=-1):
        result = []
        buffer = []

        if maxsplit == 0:
            return result.append(self.string)

        if sep is None: # Cắt chuỗi theo ký tự khoảng trắng (mặc định)
            for i in range(0, len(self.string)):    # Duyệt qua từng vị trí trong chuỗi gốc
                if self.string[i].isspace() and maxsplit != 0:
                    if i != 0:
                        result.append(''.join(buffer))
                        buffer = []
                    maxsplit -= 1
                else:
                    buffer.append(self.string[i])
            if buffer:
                result.append(''.join(buffer))
        else:   # Cắt chuỗi theo chuỗi con truyền vào
            if not sep: # Trường hợp sep rỗng
                return ValueError("Chuỗi cắt rỗng!")
            
            sep_len = len(sep)
            string_len = len(self.string)
            i = 0

            while i < string_len:   # Duyệt qua từng vị trí trong chuỗi gốc
                if self.string[i:i + sep_len] == sep and maxsplit != 0:
                    if i != 0:
                        result.append(''.join(buffer))
                        buffer = []
                    maxsplit -= 1
                    i += sep_len
                else:
                    buffer.append(self.string[i])
                    i += 1
            if buffer:
                result.append(''.join(buffer))

        return result
    



    # Clone lại phương thức rsplit() của lớp str
    """ Techniques:
    > Slicing
    > `lc` parameter
    > Giá trị mặc nhiên None
    """
    def cl_rsplit(self, sep=None, maxsplit=-1):
        result = []
        lc = len(self.string)   # Vị trị bị cắt gần nhất

        if sep is None: # Cắt chuỗi theo ký tự khoảng trắng (mặc định)
            for i in range(len(self.string) - 1, -1, -1):
                if self.string[i].isspace():  # Kiểm tra vị trí hiện tại có cắt hay không
                    if i != len(self.string) - 1:
                        result.insert(0, self.string[i + 1:lc])
                    lc = i
                    maxsplit -= 1
                if maxsplit == 0:
                    break
            if lc != 0:
                result.insert(0, self.string[0:lc])
        else:   # Cắt chuỗi theo chuỗi con truyền vào
            if not sep:
                raise ValueError("Chuỗi cắt rỗng")
            
            i = lc - len(sep)

            while i >= 0 and maxsplit != 0:
                if self.string[i:i + len(sep)] == sep: # Kiểm tra vị trí hiện tại có cắt hay không
                    if i != len(self.string) - 1:
                        result.insert(0, self.string[i + len(sep):lc])
                    lc = i
                    maxsplit -= 1
                    i -= len(sep)
                else:
                    i -= 1
            if lc != 0:
                result.insert(0, self.string[0:lc])

        return result
    



    # Clone lại phương thức isalpha() của lớp str
    """ Techniques:
    > Generator Expression
    """
    def cl_isalpha(self):
        if not self.string:
            return False
        
        return all(unicodedata.category(char).startswith("L") for char in self.string)
    



    # Clone lại phương thức capitalize() của lớp str
    """ Techniques:
    > Slicing
    > Concatenate
    """
    def cl_capitalize(self):
        return self.string[0].upper() + self.string[1:].lower()
    



    # Clone lại phương thức swapcase() của lớp str
    """ Techniques:
    > Ternary Operator
    > Generator Expression
    """
    def cl_swapcase(self):
        return ''.join(char.lower() if char.isupper() else char.upper() for char in self.string)
    



    # Clone lại phương thức index() của lớp str
    """ Techniques:
    > Ternary Operator
    > Slicing
    """
    def cl_index(self, s, start=0, end=None):

        if s is None:
            raise ValueError("Chuỗi con không hợp lệ!")
        
        if s == '':
            return 0
        
        if end is None:
            end = len(self.string)

        start = max(0, len(self.string) + start) if start < 0 else start
        end = max(0, len(self.string) + end) if end < 0 else end

        for i in range(end - len(s)):
            if self.string[i:i + len(s)] == s:
                return i
            
        raise ValueError("Không tìm thấy chuỗi con!")
    



    # Clone lại phương thức rindex() của lớp str
    """ Techniques:
    > Ternary Operator
    > Slicing
    """
    def cl_rindex(self, s, start=0, end=None):
        if s is None:
            raise ValueError("Chuỗi con không hợp lệ!")
        
        if s == '':
            return len(self.string)
        
        if end is None:
            end = len(self.string)

        start = max(0, len(self.string) + start) if start < 0 else start
        end = max(0, len(self.string) + end) if end < 0 else end

        for i in range(end - len(s), start - 1, -1):
            if self.string[i:i + len(s)] == s:
                return i
        
        raise ValueError("Không tìm thấy chuỗi con!")




# Main function
if __name__ == '__main__':
    s = cl_Str('hello world')
    # s = cl_Str('-')
    print(s.cl_rindex(''))
    exit(0)