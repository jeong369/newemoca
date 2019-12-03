# csv to json

1. git clone "https://github.com/maur1th/csv2json-fixture.git"
2. 코드 수정
    ```
      for row in reader:
    # print(row)

    row = list(row[0].split(','))
    print(row)
    temp = [0]*6
    if len(row) != 6 :
      temp[0] = row[0]
      temp[1] = (', ').join(row[1:-4])
      temp[2:] = row[-4:]
      row = temp
    print('row', temp)
    if not header_row:
      header_row = row
      print(header_row)
      continue

    print(row)
    pk = int(row[0])
    model = model_name
    fields = {}
    print(len(row))
    for i in range(len(row) - 1):
      active_field = row[i+1] if row[i+1] != '' else ''
      ```
3. [csv2json-fixture folder] python manage.py filename.csv bigfive.Test
4. [project folder] python manage.py loaddata bigfive/fixtures/filename.json