import pandas as pd
men = pd.read_csv('men_results.csv')
women = pd.read_csv('women_results.csv')

men['date_datetime'] = men['date'].astype('datetime64[ns]')
men['gender'] = 'men'
men['tot_goals'] = men['home_score'] + men['away_score']
men_subset = men[(men['date_datetime'] >= '2002-01-01') & (men['tournament'] == 'FIFA World Cup')]
men_pop = men_subset[['gender','tot_goals']]
#print(men_pop['tot_goals'].mean())

women['date_datetime'] = women['date'].astype('datetime64[ns]')
women['gender'] = 'women'
women['tot_goals'] = women['home_score'] + women['away_score']
women_subset = women[(women['date_datetime'] >= '2002-01-01') & (women['tournament'] == 'FIFA World Cup')]
women_pop = women_subset[['gender','tot_goals']]
#print(women_subset)

data_set = pd.concat([men_pop, women_pop],ignore_index=True)
print(data_set)



import matplotlib.pyplot as plt
import seaborn as sns
import pingouin

sns.histplot(data=data_set[data_set['gender']=='men'], x="tot_goals", binwidth=1)
plt.show()
print(men_pop['tot_goals'].mean())
sns.histplot(data=data_set[data_set['gender']=='women'], x="tot_goals", binwidth=1)
plt.show()
print(women_pop['tot_goals'].mean())
# not normally distributed

alpha = 0.1
# one sided test uses significance lvl as is for alpha

# Convert weight_vs_late into wide format
data_set_wide = data_set.pivot(columns='gender', values='tot_goals')

#women first since test is women is greater than men.
wmw_test = pingouin.mwu(x=data_set_wide['women'],
	y=data_set_wide['men'],
	alternative='greater'
	)
print(wmw_test)
p_val = wmw_test['p-val'].iloc[0]


#test_results = pingouin.ttest(x=men_pop['tot_goals'], 
#	y=women_pop['tot_goals'],
#	alternative="two-sided"
#	)
#p_val = test_results['p-val'].iloc[0]

if p_val <= alpha:
	result =  "reject"
else:
	result = "fail to reject"
# if TRUE Reject Null Hypoth in favor of Alt Hypoth

result_dict = {"p_val": p_val, "result": result}
print(result_dict)

