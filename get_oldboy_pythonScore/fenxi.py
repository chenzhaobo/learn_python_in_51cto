import json
with open('result.txt','r') as f:
    for i in f:
        list1 = json.dumps(i)

list1=[["35", "501193747", "170", "B+", "D", "D", "B+", "N/A"], ["41", "442172369", "340", "B+", "B+", "B+", "B+", "N/A"], ["2", "813231615", "155", "B-", "B+", "D", "D", "N/A"], ["17", "27206461", "0", "D", "D", "D", "D", "N/A"], ["23", "894725902"], ["3", "434330017", "180", "D", "A", "A", "D", "N/A"], ["29", "15308403545", "345", "A", "B+", "B+", "B+", "N/A"], ["21", "1172861184", "290", "B", "B", "C", "B", "N/A"], ["1", "493513100", "225", "B-", "B-", "D", "B+", "N/A"], ["no name 1", "237385255"], ["14", "5272689", "370", "A", "A", "A+", "A", "N/A"], ["30", "2547788", "0", "D", "D", "D", "D", "N/A"], ["9", "1016150581", "0", "D", "D", "D", "D", "N/A"], ["31", "118146449", "350", "B+", "A", "A", "B+", "N/A"], ["5", "378777322", "245", "B", "B+", "D", "B", "N/A"], ["38", "109368424", "345", "A", "B+", "B+", "B+", "N/A"], ["7", "710275039", "355", "A", "A", "B+", "A", "N/A"], ["25", "1241424377", "335", "B", "B+", "A", "B", "N/A"], ["39", "584641574", "335", "B", "B+", "A", "B", "N/A"], ["28", "178569706", "250", "A", "A", "B-", "D", "N/A"], ["13", "437512689", "355", "B+", "A", "A", "A", "N/A"], ["16", "121440150", "250", "B+", "B", "B+", "D", "N/A"], ["33", "972102425", "0", "D", "D", "D", "D", "N/A"], ["26", "290070744", "330", "B", "B", "B+", "B+", "N/A"], ["37", "676596084", "0", "N/A", "N/A", "D", "D", "N/A"], ["42", "805824493", "85", "N/A", "N/A", "D", "B+", "N/A"], ["27", "290528767", "220", "B+", "B+", "C", "D", "N/A"], ["36", "384526074", "140", "B", "C+", "D", "D", "N/A"], ["4", "409966346", "0", "D", "D", "D", "D", "N/A"], ["32", "369545989", "370", "A", "A", "A+", "A", "N/A"], ["24", "634086977", "0", "D", "D", "D", "D", "N/A"], ["20", "33532767", "80", "B", "D", "D", "D", "N/A"], ["40", "523405048", "0", "N/A", "N/A", "D", "D", "N/A"], ["6", "295964805", "260", "B+", "A", "D", "B+", "N/A"], ["8", "114648340", "380", "A", "A+", "A+", "A", "N/A"], ["11", "307126079", "0", "D", "D", "D", "D", "N/A"], ["18", "763227", "255", "B", "A", "D", "B+", "N/A"], ["22", "642445498", "265", "A", "A", "D", "B+", "N/A"], ["34", "610550690", "330", "B", "B+", "B", "B+", "N/A"], ["19", "244131566", "245", "B", "B", "B+", "D", "N/A"], ["15", "776214156", "345", "B+", "B+", "A", "B+", "N/A"], ["10", "1205645845", "70", "B-", "D", "D", "D", "N/A"]]

x = ['A+','A','B+','B','B-','C+','C','C-','D','N/A','COPY','FAIL']
d = {}
for i in list1:
    if len(i) >2:
        d.setdefault(i[0],{})
        d[i[0]].setdefault('qq',i[1])
        for j in x:
            temp = i.count(j)
            d[i[0]].setdefault(j,temp)
k ={}
for i in list1:
    if len(i) >2:
        k.setdefault(int(i[2]),i[0])           
keys = list(k.keys())
keys.sort()
for i in keys:
    print('学号:',k[i],'    总分：',i)