from utils.data_util import data_util
from utils.pandas_util import pandas_util
from utils.visualization_util import visualization_util

class covid_analysis_chart(data_util, pandas_util, visualization_util):

    def __init__(self, filename):
        self.df = self.read_a_csv(filename)

    def plot_top10_confirmed_bar(self):
        df1 = self.df[['Country/Region','Confirmed']].nlargest(10, 'Confirmed')
        self.plot_chart(chart_type='bar', x=df1['Country/Region'], y=df1['Confirmed'])

    def plot_death_distribution_pie(self):
        self.df2 = self.get_sum_from_grouped_df(self.group_dataFrame(self.df, 'WHO Region'), 'Deaths')
        self.plot_chart(chart_type='pie', x=self.df2.index, y=self.df2.values, title='Death Distribution by WHO Region', autopct='%1.0f%%')

    def plot_top5_confirmed_vs_deaths_line(self):
        df3 = self.df[['Country/Region','Confirmed','Deaths']].nlargest(5, 'Confirmed')
        self.plot_chart(chart_type="line", x=df3["Country/Region"], y={"Confirmed": df3["Confirmed"],"Deaths": df3["Deaths"]}, title="Top 5 Countries: Confirmed vs Deaths", xlabel="Country/Region",ylabel="Number of Cases", multi_plot=True)

    def plot_confirmed_vs_recovered_scatter(self):
        self.plot_chart(chart_type='scatter', x=self.df['Confirmed'], y=self.df['Recovered'], title='Confirmed vs Recovered Cases', xlabel='Confirmed Cases', ylabel='Recovered Cases', c=self.df['Recovered'], cmap='rainbow_r', alpha=0.6)

    def plot_death_counts_hist(self):
        self.plot_chart(chart_type='hist', x=self.df2.values, title='Distribution of Death Counts by WHO Region', xlabel='Number of Deaths', ylabel='Frequency', bins=10, color='purple', edgecolor='black')

    def plot_confirmed_deaths_recovered_stacked_bar(self):
        df6 = self.df[['Country/Region','Confirmed','Deaths','Recovered']].head(5)
        self.plot_chart(chart_type="stacked_bar", data=df6 ,x="Country/Region",   y=["Confirmed","Deaths","Recovered"], title="Stacked Bar Chart", xlabel='Country/Region', ylabel='Number of Cases', grid=True, label = ["Confirmed","Deaths","Recovered"])
    
    def plot_confirmed_boxplot_by_region(self):
        self.plot_chart(chart_type='box', x = 'WHO Region',  y = 'Confirmed', data =self.df,title='Boxplot of Confirmed Cases by WHO Region', xlabel='WHO Region', ylabel='Number of Confirmed Cases')

    def plot_india_vs_country_trend(self, country):
        india = self.df[self.df['Country/Region'] == 'India'][['Confirmed','Deaths','Recovered']].iloc[0]
        other_country = self.df[self.df['Country/Region'] == country][['Confirmed','Deaths','Recovered']].iloc[0]
        categories = ['Confirmed','Deaths','Recovered']
        self.plot_chart(chart_type="line", x = categories, y={"India": india.values, country : other_country.values}, title="Covid Cases Comparison: India vs " + country, xlabel="Number of Cases", multi_plot=True)        

   
if __name__ == "__main__":
    covid_analysis = covid_analysis_chart('./Week 5/data/country_wise_latest.csv')
    covid_analysis.plot_top10_confirmed_bar()
    covid_analysis.plot_death_distribution_pie()
    covid_analysis.plot_top5_confirmed_vs_deaths_line()
    covid_analysis.plot_confirmed_vs_recovered_scatter()
    covid_analysis.plot_death_counts_hist()
    covid_analysis.plot_confirmed_deaths_recovered_stacked_bar()
    covid_analysis.plot_confirmed_boxplot_by_region()
    covid_analysis.plot_india_vs_country_trend("Algeria")