import pandas as pd
import matplotlib.pyplot as plt
import random



class visualization_util:

    def plot_chart(self, chart_type, x, y=None, data = None, title=None, xlabel=None, ylabel=None, rotation=30, grid=True, multi_plot = None , **user_params):
        
        if chart_type == "bar":
            additional_param = {"width": 0.7, "align": "center", "edgecolor": "black"}
            additional_param.update(user_params)
            plt.bar(x, y, **additional_param)

        elif chart_type == "line":
            if multi_plot:
                for label, y_values in y.items():
                    additional_param = {"linestyle": "--", "linewidth": 2, "marker": random.choice(["o", "x", "s", "d", "^", "v", "<", ">", "p", "*"])}
                    additional_param.update(user_params)
                    plt.plot(x, y_values,label=label, **additional_param)
            else:
                additional_param = {"linestyle": "--", "linewidth": 2, "marker": "o"}
                additional_param.update(user_params)
                plt.plot(x, y, **additional_param)

        elif chart_type == "scatter":
            additional_param = {"s": 100, "marker": "o", "edgecolor": "black", "cmap": "viridis"}
            additional_param.update(user_params)
            plt.scatter(x, y, **additional_param)
            plt.colorbar()

        elif chart_type == "hist":
            additional_param = {"bins": 10, "edgecolor": "black", "histtype": "bar"}
            additional_param.update(user_params)
            plt.hist(x, **additional_param)

        elif chart_type == "pie":
            additional_param = {"autopct": "%1.1f%%", "startangle": 90,}
            additional_param.update(user_params)
            plt.pie(y, labels=x, **additional_param)
        
        elif chart_type == "box":
            additional_param = {}
            additional_param.update(user_params)
            data.boxplot(by = x, column=y, **additional_param)

        elif chart_type == "stacked_bar":
            bottom = 0
            for col in y:
                plt.bar(data[x], data[col], bottom=bottom, label=col)
                bottom = bottom + data[col]

        else:
            raise ValueError("Invalid chart_type. Use: bar, line, scatter, hist, pie, box, stacked_bar")
        
        if title:
            plt.title(title)

        if xlabel and chart_type not in ["pie", "hist"]:
            plt.xlabel(xlabel)

        if ylabel and chart_type not in ["pie"]:
            plt.ylabel(ylabel)

        if rotation and chart_type not in ["pie"]:
            plt.xticks(rotation=rotation)
        
        if grid and chart_type not in ["pie"]:
            plt.grid(True, linestyle="--", alpha=0.6)

        if user_params.get("label") or multi_plot:
            plt.legend()

        plt.tight_layout()
        plt.show()