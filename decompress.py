import olefile

ole = olefile.OleFileIO('test.hwp')
# ole 디렉터리 출력
print(ole.listdir())

stream = ole.openstream('BIN0001.eps')
print(stream)