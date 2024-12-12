#5
def m_stroka(row):
  sum = 0
  for element in row:
    sum += element
  return sum

def min_max(row):
  return min(row), max(row)

arr = [[3, 1, 4], [1, 5 , 7], [7, 0, 0], [9,3,6]]
s = list()

for row in arr:
  sum_of_row = m_stroka(row)
  s.append(sum_of_row)

print(s,'\n',r'max is', max(row), 'sum is', max(s), '\n',r'min is', min(row), 'sum is', min(s))


#6
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_arr = []

for row in arr:
    min_el = min(row)
    row_copy = row[:]
    for i in range(len(row_copy)):
        if row_copy[i] == min_el:
            row_copy[i] = row_copy[i]%2
            break
    new_arr.append(row_copy)

for row in new_arr:
    print(row)

