import pandas as pd
#1 задание
def proportion_of_education(df):
  len_df = len(df)
  less12 = float(df['EDUC1'].where(df['EDUC1']==1).count()/len_df)
  educ12 = float(df['EDUC1'].where(df['EDUC1']==2).count()/len_df)
  more12 = float(df['EDUC1'].where(df['EDUC1']==3).count()/len_df)
  college = float(df['EDUC1'].where(df['EDUC1']==4).count()/len_df)
  result = {"less than 12": less12,
            "education 12": educ12,
            "more than 12": more12,
            "college education": college}
  print(result)
df = pd.read_csv('NISPUF17.csv', sep=',')
proportion_of_education(df)

df = pd.read_csv('NISPUF17.csv', sep=',')
df['CBF_01'] = df['CBF_01'].replace(1, 'vac', regex = True)
df['CBF_01'] = df['CBF_01'].replace(2, 'nvac', regex = True)
df['CBF_01'] = df['CBF_01'].replace(99, 'dontknow', regex = True)
df['CBF_01'] = df['CBF_01'].replace(77, 'miss', regex = True)
bm = df.groupby('CBF_01')['P_NUMFLU'].mean()
bm_tuple = (round(float(bm[1]), 1), round(float(bm[2]), 1))
print(bm_tuple)

#2 задание
df = pd.read_csv('NISPUF17.csv', sep=',')
df['CBF_01'] = df['CBF_01'].replace(1, 'yes', regex=True)
df['CBF_01'] = df['CBF_01'].replace(2, 'no', regex=True)
df['CBF_01'] = df['CBF_01'].replace(77, 'dk', regex=True)
df['CBF_01'] = df['CBF_01'].replace(99, 'miss', regex=True)

bm = df.groupby('CBF_01')['P_NUMFLU'].mean()
bm_tuple = (round(float(bm[1]), 1), round(float(bm[2]), 1))
print(bm_tuple)

#3 задание
df = pd.read_csv("NISPUF17.csv", sep=',')
dfMale = df[df["SEX"] == 1]
dfFemale = df[df["SEX"] == 2]

maleCpx = dfMale[(dfMale["HAD_CPOX"] == 1) & (dfMale["P_NUMVRC"] > 0)].shape[0]/dfMale[(dfMale["HAD_CPOX"] == 2) & (dfMale["P_NUMVRC"] > 0)].shape[0]
femaleCpx = dfFemale[(dfFemale["HAD_CPOX"] == 1) & (dfFemale["P_NUMVRC"] > 0)].shape[0]/dfFemale[(dfFemale["HAD_CPOX"] == 2) & (dfFemale["P_NUMVRC"] > 0)].shape[0]

print(
    {"male": round(maleCpx, 4),
        "female": round(femaleCpx, 4)}
)
