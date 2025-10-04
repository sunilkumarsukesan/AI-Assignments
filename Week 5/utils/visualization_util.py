import pandas as pd
import matplotlib.pyplot as plt


class visualization_util:

    def plot_chart(self, kind, x, y=None, data = None, title=None, xlabel=None, ylabel=None, rotation=30, grid=True, **user_params):

            
        if kind == "bar":
            params = {"width": 0.7, "align": "center", "edgecolor": "black"}
            params.update(user_params)
            plt.bar(x, y, **params)

        elif kind == "line":
            params = {"linestyle": "-", "linewidth": 2, "marker": "o"}
            params.update(user_params)
            plt.plot(x, y, **params)

        elif kind == "scatter":
            params = {"s": 100, "marker": "o", "edgecolor": "black", "cmap": "viridis"}
            params.update(user_params)
            plt.scatter(x, y, **params)
            plt.colorbar()

        elif kind == "hist":
            params = {"bins": 10, "edgecolor": "black", "histtype": "bar"}
            params.update(user_params)
            plt.hist(x, **params)

        elif kind == "pie":
            params = {"autopct": "%1.1f%%", "startangle": 90}
            params.update(user_params)
            plt.pie(y, labels=x, **params)

        
        elif kind == "box":
            params = {}
            params.update(user_params)
            data.boxplot(by = x, column=y, **params)


        else:
            raise ValueError("Invalid kind. Use: bar, line, scatter, hist, pie")
        
        if title:
            plt.title(title)

        if xlabel and kind not in ["pie", "hist"]:
            plt.xlabel(xlabel)

        if ylabel and kind not in ["pie"]:
            plt.ylabel(ylabel)

        if rotation and kind not in ["pie"]:
            plt.xticks(rotation=rotation)
        
        if grid and kind not in ["pie"]:
            plt.grid(True, linestyle="--", alpha=0.6)

        if user_params.get("label"):
            plt.legend()

        plt.tight_layout()
        plt.show()
    

    def plot_country_trend(df, countries, metric):
        plt.figure(figsize=(10,6))

        for country in countries:
            country_data = df[df['Country/Region'] == country]
            plt.plot(country_data['Date'], country_data[metric], marker="o", linestyle="--", label=country)

        plt.title(f"{metric} Cases Trend: {' vs '.join(countries)}")
        plt.xlabel("Date")
        plt.ylabel(f"Number of {metric} Cases")
        plt.xticks(rotation=45)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()