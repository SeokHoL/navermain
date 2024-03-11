import csv
import re

csv_file_path ='C:\\navernew\\불법주정차 신고현황(22.11월~23.10월).csv'
new_csv =[]
with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_dict=csv.DictReader(file)
    pattern = re.compile(r'\b\w*용산\w*\b')
    for row in csv_dict:
        # 각 열에 대한 값에 접근하여 출력
        if pattern.findall(row['주소']):
            print(row['\ufeff"민원접수일"'],row['민원접수시간'],row['주소'])
            new_csv.append({"민원접수일" : row['\ufeff"민원접수일"'],"민원접수시간":row['민원접수시간'],"주소":row['주소']})

csv_file_path2 ='C:\\navernew\\불법주정차 신고현황(22.11월~23.10월)remake.csv'
with open(csv_file_path2,'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)

    # 헤더 쓰기
    header = new_csv[0].keys()
    csv_writer.writerow(header)

    # 데이터 쓰기
    for row in new_csv:
        csv_writer.writerow(row.values())
