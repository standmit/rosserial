class ParserBuffer:
    def __init__(
            self,
            read_func
    ):
        self._read_func = read_func
        self._buffer = []
        self._read_pos = 0
    
    def read(self, count):
        buflen = len(self._buffer) - self._read_pos
        if buflen < count:
            self._buffer.extend(self._read_func(count - buflen))
        read_pos = self._read_pos
        self._read_pos += count
        return self._buffer[read_pos:self._read_pos]
    
    def commit(self):
        self._buffer = self._buffer[self._read_pos:]
        self._read_pos = 0
    
    def rollback(self):
        self._read_pos = 0