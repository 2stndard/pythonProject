import pandas as pd
from dfply import *
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_list = [font.name for font in fm.fontManager.ttflist]
font_list

df_입학생 = pd.read_excel('C:/R/git/datavisualization/chap3/2021_연도별_입학자수.xlsx', sheet_name='Sheet0', header=(1, 2),
                       nrows=400)
df_입학생.head()
df_입학생.info()
df_입학생.describe()
df_입학생.loc[1:5]
df_입학생 = df_입학생.iloc[:, [0, 1, 2, 4, 8, 28, 30]]
df_입학생.shape[0]

df_입학생.index
df_입학생 = df_입학생 >> select(0, 1, 2, 4, 8, 28, 30)
df_입학생.columns = ['연도', '시도', '전체', '전문대', '일반대', '석사', '박사']

df_입학생_전체 = df_입학생 >> filter_by(X.시도 == '전체')
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Malgun Gothic'
sns.lineplot(x='연도', y='전체', data=df_입학생_전체)
