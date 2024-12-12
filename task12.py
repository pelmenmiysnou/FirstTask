#задание 4
df = pd.read_csv('Mall_Customers.csv', sep=',').where(df['Genre']=='Male')
df = df.dropna()
plt.bar(df['Age'], df['Annual Income (k$)'], label="бла блоа боа")
plt.xlabel('age')
plt.ylabel('annual income')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()


#задание 5
df = pd.read_csv('Mall_Customers.csv', sep=',')
males = df.where(df['Genre']=='Male')
females = df.where(df['Genre']=='Female')
males = males.dropna()
females = females.dropna()
plt.bar(males['Spending Score (1-100)'], males['Annual Income (k$)'],color = 'red')
plt.bar(females['Spending Score (1-100)'], females['Annual Income (k$)'],color = 'blue')
plt.xlabel('spending score (1-100)')
plt.ylabel('annual income')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()
