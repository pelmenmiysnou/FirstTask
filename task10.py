#4
my_list1 = []
my_list2 = []
for i in range(4):
  for j in range(10):
    my_list1.append(i*10 + 10 - j)
    my_list2.append(i*10 + 10 + j)
df1 = pd.DataFrame([my_list1[i:i+10] for i in range(0, len(my_list1), 10)], columns=[f'column{i}' for i in range(10)])
df2 = pd.DataFrame([my_list2[i:i+10] for i in range(0, len(my_list2), 10)], columns=[f'column{i}' for i in range(10)])
print(df1,'\n',df2)
df_concat = pd.concat([df1, df2])
print(df_concat)

df_merge = pd.merge(df1, df2, left_index = True, right_index = True, suffixes=('_df1', '_df2'))
print(df_merge)


#5
my_list1 = []
my_list2 = []
for i in range(4):
  for j in range(10):
    my_list1.append(i*10 + 10 - j)
    my_list2.append(i*10 + 10 + j)
df1 = pd.DataFrame([my_list1[i:i+10] for i in range(0, len(my_list1), 10)], columns=[f'column{i}' for i in range(10)])
df2 = pd.DataFrame([my_list2[i:i+10] for i in range(0, len(my_list2), 10)], columns=[f'column{i}' for i in range(10)])

plt.figure(figsize=(12, 6))
for i in range(10):
    plt.plot(df1[f'column{i}'], df2['column0'], marker='o', linestyle='-', color='b', label=f'Column {i}' if i == 0 else "")
plt.title("Зависимость столбцов из df1 от первого столбца из df2")
plt.xlabel("Значения из столбцов df1")
plt.ylabel("Значения из нулевого столбца df2")
plt.legend()
plt.grid(True)
plt.show()
