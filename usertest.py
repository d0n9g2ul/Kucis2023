#-*- encoding: utf-8 -*-

import alpha as AL


def main():

    #객체 생성
    al = AL.ALPHA()
    log = AL.extract(path="/log", stdate="yy-mm-dd", eddate="yy-mm-dd")
    #csv 파일 생성 // if file == 1개
    log_file = al.change_csv('access.log.txt') #결과는 access.log.txt가 access.log.csv변환

    #날짜별로 부분 클론 생성 // file을 쪼개고 싶을 때 => 하루단위
    logfile_split = al.split("access.log.txt")

    #특정 날짜 부분 합친 파일 생성 // 폴더 밑에 있는 파일들 중에 변수에 해당하는 날짜를 하나로 합친 파일 생성
    logfile_zip = al.zipper(stdate="yy-mm-dd", eddate="yy-mm-dd")

    #필터
    log = logfile_zip.filter(ip="203.237.211.217", method="get") #string="문자열", ip ="아이피", date="날짜", method="get or post", response="200"

    #order_by
    log = log.order_by(param="param",desc=True) # desc=True: 오름차순 param="string", param="ip"

    #counter
    log_count = log.count() # 총 개수

    #limit
    log_limit_1 = log.limit(1)




if __name__ == '__main__':
    main()
