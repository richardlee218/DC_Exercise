crimes['HOUR OCC'] = crimes['TIME OCC'].str[:2].astype(int)

sns.countplot(x='HOUR OCC', data=crimes)
plt.show()

peak_crime_hour = 12


night_crimes = crimes[(crimes['HOUR OCC'] >= 22) & (crimes['HOUR OCC'] < 24) | (crimes['HOUR OCC'] >= 0) & (crimes['HOUR OCC'] < 4)]
#print(night_crimes)

night_freq = night_crimes.groupby('AREA NAME')['HOUR OCC'].count()
peak_night_crime_location = night_freq.sort_values( axis=0 ,ascending=False).index[0]
print(peak_night_crime_location)


vict_age_subset = crimes[["Vict Age"]]

labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
bins = [0,17,25,34,44,54,64,np.inf]

vict_age_subset["victim_age_bins"] = pd.cut(x=vict_age_subset["Vict Age"], labels=labels, bins=bins)
vict_bin_series = pd.cut(x=vict_age_subset["Vict Age"], labels=labels, bins=bins)
victim_ages = vict_bin_series.value_counts()

print(victim_ages)



