from utils.data_util import data_util
from utils.pandas_util import pandas_util
from utils.visualization_util import visualization_util

class covid_analysis_chart(data_util, pandas_util,visualization_util):

    def __init__(self, filename):
        self.df = self.read_a_csv(filename)

    def plot_top10_confirmed_bar(self):
        df1 = self.df[['Country/Region','Confirmed']].nlargest(10, 'Confirmed')
        visualization_util().plot_chart(kind='bar', x=df1['Country/Region'], y=df1['Confirmed'], title='Top 10 Countries by Confirmed Cases', xlabel='Country/Region', ylabel='Number of Confirmed Cases', rotation=45, color='orange', edgecolor='black')

    def plot_death_distribution_pie(self):
        df2 = self.df.groupby('WHO Region')['Deaths'].sum()
        visualization_util().plot_chart(kind='pie', x=df2.index, y=df2.values, title='Death Distribution by WHO Region', autopct='%1.1f%%')

    def plot_top5_confirmed_vs_deaths_line(self):
        df3 = self.df[['Country/Region','Confirmed','Deaths']].nlargest(5, 'Confirmed')
        visualization_util().plot_chart(kind='line', x=df3['Country/Region'], y=df3['Confirmed'], title='Top 5 Countries: Confirmed vs Deaths', xlabel='Country/Region', ylabel='Number of Cases', color='blue', marker='o', label='Confirmed')
        visualization_util().plot_chart(kind='line', x=df3['Country/Region'], y=df3['Deaths'], color='red', marker='x', label='Deaths')

    def plot_confirmed_vs_recovered_scatter(self):
        visualization_util().plot_chart(kind='scatter', x=self.df['Confirmed'], y=self.df['Recovered'], title='Confirmed vs Recovered Cases', xlabel='Confirmed Cases', ylabel='Recovered Cases', c=self.df['Recovered'], cmap='rainbow_r', alpha=0.6)

    def plot_death_counts_hist(self):
        df5 = self.df.groupby('WHO Region')['Deaths'].sum()
        visualization_util().plot_chart(kind='hist', x=df5.values, title='Distribution of Death Counts by WHO Region', xlabel='Number of Deaths', ylabel='Frequency', bins=10, color='purple', edgecolor='black')

    def plot_confirmed_deaths_recovered_stacked_bar(self):
        df6 = self.df[['Country/Region','Confirmed','Deaths','Recovered']].head(5)
        visualization_util().plot_chart(kind='bar', x=df6['Country/Region'], y=None, title='Top 5 Countries: Confirmed, Deaths, and Recovered Cases', xlabel='Country/Region', ylabel='Number of Cases', rotation=45)
        visualization_util().plot_chart(kind='bar', x=df6['Country/Region'], bottom=df6['Confirmed'], label='Deaths', color='salmon')  # To initialize the bar chart
        visualization_util().plot_chart(kind='bar', x=df6['Country/Region'], bottom=df6['Confirmed']+df6['Deaths'], label='Recovered', color='lightgreen')  # To initialize the bar chart
    
    def plot_confirmed_boxplot_by_region(self):
        visualization_util().plot_chart(kind='box', x = 'WHO Region',  y = 'Confirmed', data =self.df,title='Boxplot of Confirmed Cases by WHO Region', xlabel='WHO Region', ylabel='Number of Confirmed Cases')

    def plot_india_vs_country_trend(self):
        visualization_util.plot_country_trend(self.df, countries=['India', 'Algeria'], metric='Confirmed')

   
if __name__ == "__main__":
    covid_analysis = covid_analysis_chart('./Week 5/data/country_wise_latest.csv')
    covid_analysis.plot_top10_confirmed_bar()
    covid_analysis.plot_death_distribution_pie()
    covid_analysis.plot_top5_confirmed_vs_deaths_line()
    covid_analysis.plot_confirmed_vs_recovered_scatter()
    covid_analysis.plot_death_counts_hist()
    covid_analysis.plot_confirmed_deaths_recovered_stacked_bar()
    covid_analysis.plot_confirmed_boxplot_by_region()
    covid_analysis.plot_india_vs_country_trend()