from utils.data_util import data_util
from utils.pandas_util import pandas_util

class covid_analysis(data_util, pandas_util):

    def __init__(self, filename):
        self.df = self.read_a_csv(filename)

    def case_count_by_region(self):
        return self.get_sum_from_grouped_df(self.group_dataFrame(self.df,['WHO Region', 'Country/Region']),['Confirmed', 'Deaths','Recovered'])

    def filter_low_case_record(self):
        return self.df[self.df['Confirmed'] >= 10]
    
    def highest_confirmed_cases(self):
        return self.df.loc[self.get_index_of_extreme(self.df,'Confirmed'), 'Country/Region']
    
    def sort_data_by_confirmed_cases_export(self):
        self.write_to_csv(self.df.iloc[self.get_sorted_index(self.df,'Confirmed')], "./Week 4/ExportedFiles/sorted_data.csv")
        print("Export successful!")

    def top_5_countries_by_case_count(self):
        return self.df.iloc[self.get_sorted_index(self.df,'Confirmed') [::-1] [:5]]
    
    def region_with_lowest_death_count(self):
        return self.df['Country/Region'] [self.df['Deaths'] == self.df['Deaths'].min()]
    
    def india_case_summary(self):
        return self.df[self.df['Country/Region'] == 'India']

    def mortality_rate(self):
        self.df['Mortality Rate'] = (self.df['Deaths'] / self.df['Confirmed']) * 100
        return self.df[['Country/Region','Mortality Rate']]
    
    def recovery_rate(self):
        return self.df[['Country/Region','Recovered / 100 Cases']]
    
    def get_non_outliers_case_counts(self):
        return self.df[self.get_non_outliers(self.df,'Confirmed')]
    

    def group_data_by_country_and_region(self):
        return self.group_dataFrame(self.df,['WHO Region','Country/Region']).size()
    
    def region_with_zero_recovered_cases(self):
        return self.df[self.df['Recovered'] == 0]

if __name__ == "__main__":
    c = covid_analysis('./Week 4/data/country_wise.csv')
    print(c.case_count_by_region())
    print(c.filter_low_case_record())
    print(c.highest_confirmed_cases())
    c.sort_data_by_confirmed_cases_export()
    print(c.top_5_countries_by_case_count())
    print(c.region_with_lowest_death_count())
    print(c.india_case_summary())
    print(c.mortality_rate())
    print(c.recovery_rate())
    print(c.get_non_outliers_case_counts())
    print(c.group_data_by_country_and_region())
    print(c.region_with_zero_recovered_cases())