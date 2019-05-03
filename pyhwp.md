# pyhwp 설치 
https://github.com/mete0r/pyhwp <br/>

<br/>

# anaconda  가상환경 설치
```
$ conda create -n pyhwp python=2.7 
```

<br/>

# anaconda 가상환경 활성화
```
$ source activate pyhwp
```

<br/>

# pyhwp 테스트
```
./hwp5html --output=~/test/output ~/test/sample/sample.hwp
```

# 헤더 출력
패스워드 확인 가능 <br/>
compressed: ? <br/>

```
(pyhwp)$ hwp5proc header ./samples/sample-5017.hwp
ccl: 0
cert_drm: 0
cert_encrypted: 0
cert_signature_extra: 0
cert_signed: 0
compressed: 1
distributable: 0
drm: 0
history: 0
password: 0
script: 0
signature: HWP Document File
version: 5.0.1.7
xmltemplate_storage: 0
```

# 요약 정보
제목, 

```
(pyhwp)$ hwp5proc summaryinfo ./samples/sample-5017.hwp
Title: 제목입니다.
Subject: 주제입니다.
Author: 지은이입니다.
Keywords: 키워드입니다.
Comments: 기타입니다.
Last saved by: mete0r
Revision Number: 6, 7, 9, 1053 WIN6
Last Printed at: 1601-01-01 00:00:00
Created at: 2010-07-02 03:36:13.540000
Last saved at: 2011-06-14 12:54:58.775000
Number of pages: 2
Date: 2010년 7월 2일 금요일 오후 12:36:13
Number of paragraphs: 26
```

# 스트림 목록 출력
```
(pyhwp)$ hwp5proc ls ./samples/sample-5017.hwp
\x05HwpSummaryInformation
BinData/BIN0002.jpg
BinData/BIN0002.png
BinData/BIN0003.png
BodyText/Section0
DocInfo
DocOptions/_LinkDoc
FileHeader
PrvImage
PrvText
Scripts/DefaultJScript
Scripts/JScriptVersion
```

# 구조 내용 출력
```
(pyhwp)$ hwp5proc records ./samples/sample-5017.hwp DocInfo
[
{
  "level": 0, 
  "payload": [
    "01 00 01 00 01 00 01 00 01 00 01 00 01 00 00 00", 
    "00 00 07 00 00 00 05 00 00 00"
  ], 
  "seqno": 0, 
  "size": 26, 
  "tagid": 16, 
  "tagname": "HWPTAG_DOCUMENT_PROPERTIES"
},
{
  "level": 0, 
```

# 스트림 내용 출력
```
(pyhwp)$ hwp5proc cat ./samples/sample-5017.hwp BinData/BIN0002.jpg
파일 내용이 길어 생략..
```