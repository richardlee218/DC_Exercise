import pandas as pd
import seaborn as sns
import numpy as np


folder_name = "data"
file_name = "nobel.csv"
file_path = folder_name + "/" + file_name

nobel = pd.read_csv(file_path)
print(nobel.columns)
print(nobel.head())


#print(nobel['sex'].head())
gender_cnt = nobel.groupby('sex')['sex'].count()
#print(gender_cnt)
# using groupby does not automatically sort by aggregated values.
gender_max = gender_cnt.max()
#print(gender_max)
top_gender = gender_cnt[gender_cnt == gender_max].index[0]
print( top_gender )

# using value_counts automatically sort by aggregated values.
top_country = nobel.value_counts('birth_country').index[0]
print(top_country)



nobel['decade'] = ( np.floor(nobel['year']/10) * 10 ).astype(int)
nobel['us_born'] = nobel['birth_country'] == top_country

decade_sums = nobel.groupby(['decade'],as_index=False).sum('us_born')
decade_totals = nobel.groupby(['decade'],as_index=False).count()
decade_bcountry_ratio = nobel.groupby(['decade'],as_index=False).mean('us_born')
#print(decade_bcountry_ratio[['decade','us_born']])
print(decade_bcountry_ratio['us_born'].max())
max_decade_usa = decade_bcountry_ratio.sort_values(by='us_born', ascending=False)['decade'].iloc[0]
print(max_decade_usa)


nobel['is_female'] = nobel['sex'] == "Female"
decade_fem_sums = nobel.groupby(['decade','category'],as_index=False).sum('is_female')
decade_totals = nobel.groupby(['decade','category'],as_index=False).count()
dec_cat_female_prop = nobel.groupby(['decade','category'],as_index=False).mean('is_female')
max_female_decade_cat = dec_cat_female_prop.sort_values(by='is_female', ascending=False)[['decade','category']].reset_index(drop=True)
max_female_decade_cat = max_female_decade_cat.iloc[[0]]
print(max_female_decade_cat)
max_female_dict = {max_female_decade_cat["decade"].values[0]:max_female_decade_cat["category"].values[0]}
print(max_female_dict)


female_nobel = nobel[nobel['is_female']==True]
min_fem_year = female_nobel['year'].min()
first_fem = female_nobel[female_nobel['year']==min_fem_year]
first_woman_name = first_fem['full_name'].iloc[0]
first_woman_category = first_fem['category'].iloc[0]
print(first_woman_name)
print(first_woman_category)


name_repeat_cnt = nobel.groupby('full_name')['year'].count()
name_repeat_cnt = name_repeat_cnt.sort_values(ascending=False)
name_repeat_multi_win = name_repeat_cnt[name_repeat_cnt > 1]
repeat_list = list(name_repeat_multi_win.index)
print(repeat_list)



