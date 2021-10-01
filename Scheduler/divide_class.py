emotion = []

emotion.append('문학적인') #0
emotion.append('논쟁을 좋아하는') #1
emotion.append('진취적인') #2
emotion.append('실용적인') #3
emotion.append('탐구적인') #4
emotion.append('안온한') #5
emotion.append('활동적인') #6
emotion.append('호기심 많은 ') #7

#문학적인 수업 리스트
df_0 = df.loc[df['선택영역']=='사상과역사']

#논쟁을 좋아하는 수업 리스트
df_1_0 = df.loc[df['선택영역']=='사상과역사']
df_1_1 = df.loc[df['선택영역']=='인성과창의력']
df_1_2 = df.loc[df['선택영역']=='인성과도덕']

df_1 = pd.concat([df_1_0,df_1_1,df_1_2])

#진취적인 수업 리스트
df_2_0 = df.loc[df['선택영역']=='사회와문화']
df_2_1 = df.loc[df['선택영역']=='세계와지구촌']

df_2 = pd.concat([df_2_0,df_2_1])

#실용적인 수업 리스트
df_3_0 = df.loc[df['선택영역']=='사회와제도']
df_3_1 = df.loc[df['선택영역']=='세계와지구촌']
df_3_2 = df.loc[df['선택영역']=='지구촌의이해']
df_3_3 = df.loc[df['선택영역']=='예술과생활']
df_3_4 = df.loc[df['선택영역']=='융합과창업']
df_3_5 = df.loc[df['선택영역']=='자연과과학기술']

df_3 = pd.concat([df_3_0,df_3_1,df_3_2,df_3_4,df_3_4,df_3_5])

#탐구적인
df_4_0 = df.loc[df['선택영역']=='생명과과학']
df_4_1 = df.loc[df['선택영역']=='생명과자연']
df_4_2 = df.loc[df['선택영역']=='자연과과학기술']

df_4 = pd.concat([df_4_0,df_4_1,df_4_2])

#안온한 수업 리스트
df_5 = df.loc[df['선택영역']=='역사와문화']

#활동적인 수업 리스트
df_6 = df.loc[df['선택영역']=='예술과생활']

#호기심 많은
df_7_0 = df.loc[df['선택영역']=='예술과생활']
df_7_1 = df.loc[df['선택영역']=='인성과창의력']
df_7_2 = df.loc[df['선택영역']=='인성과도덕']

df_7 = pd.concat([df_7_0,df_7_1,df_7_2])

print(df_0)
'''
df_0.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/문학적인수업.csv')
df_1.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/논쟁을좋아하는수업.csv')
df_2.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/진취적인수업.csv')
df_3.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/실용적인수업.csv')
df_4.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/탐구적인수업.csv')
df_5.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/안온한수업.csv')
df_6.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/활동적인수업.csv')
df_7.to_csv('/content/drive/MyDrive/( 2021 - 2 ) 해커톤/분류 된 수업 리스트/호기심덩어리수업.csv')
'''