import struct
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("./mnist/" + name + "-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/" + name + "-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/" + name + ".csv", "w", encoding="utf-8")
    # 1. 헤더 정보 읽기
    #  >II : big-endian 방식으로 데이터를 읽는 옵션
    #  big-endian은 주소가 큰값부터 데이터를 저장하는 방식 : Sun
    #  little-endian은 주소가 작은값부터 데이터를 저장하는 방식 : Intel
    # 파일 구조는 웹사이트에서 참고
    #  read(8) 현재 파일포인터에서 8byte 읽어들임
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_count = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols
    # 2. 이미지 데이터를 읽고 CSV로 저장하기
    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        label = struct.unpack("B", lbl_f.read(1))[0]
        # "B" => unsigned char
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label) + ",")
        csv_f.write(",".join(sdata)+"\r\n")
        # 3. 이미지 파일로 저장해서 테스트하기
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name, idx, label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()
# 4. 결과를 파일로 출력하기
to_csv("train", 3000)
# to_csv("train", 60000)
to_csv("t10k", 500)
