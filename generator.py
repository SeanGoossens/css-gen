def build():
    clearwaterColors = """"#0A5EB2",
        "#00A2E0",
        "#0B325F",
        "#008B94",
        "#56D8C2",
        "#00B7BD",
        "#B5B5B5",
        "#636363",
        "#282828",
        "#EFEFEF"
    """
    clearwaterFont = '"Arial"'

    chart = input('Chart type: ')
    width = input('Width: ')
    height = input('Height: ')
    dataLabels = input('Data labels enabled? Type true or false: ')
    legendEnabled = input('Legend enabled? Type true or false: ')

    print("""{
    "colors": [
        """ +  clearwaterColors + """], 
    
    "chart": {
        "type": """ +
          '"' + chart + '",' + """
        "width": """ + width + ',' + """
        "height": """ + height + ',' + """
        "style": {
            "fontfamily": """ + clearwaterFont + """
            },
        "spacingTop": 0,
        "spacingRight": 0,
        "spacingLeft": 0,
        "spacingBottom": 0,
        "renderTo": "highchartContainer"
    },
    
    "plotOptions": {
        "series": {
            "dataLabels": {
                "enabled": """ + dataLabels + """,
                "format": "{y}",
                "padding": 2,
                "style": {
                    "fontSize": "8px",
                    "letterSpacing": ".05px",
                    "textShadow": "false"
                },
                "color": "#4d4d4f",
                "y": -2
            }
        },
        "column": {
            "borderWidth": 0,
            "groupPadding": 0.06,
            "pointPadding": 0,
            "pointRange": 0
        }
    },
    "title": {
        "text": null
    },
    "yAxis": {
        "title": {
            "text": null
        },
        "lineWidth": 0.5,
        "lineColor": "#a7a9ac",
        "tickColor": "#a7a9ac",
        "tickPosition": "inside",
        "tickPositions": "",
        "tickWidth": 0.5,
        "tickLength": 4,
        "gridLineWidth": 0,
        "gridLineInterpolation": null,
        "labels": {
            "enabled": true,
            "x": -5,
            "format": "{value}%",
            "style": {
                "fontSize": "8px",
                "color": "#4d4d4f"
            }
        },
        "type": "value"
    },
    "legend": {
        "enabled": """ + legendEnabled + """,
        "align": "right",
        "verticalAlign": "top",
        "itemStyle": {
            "fontWeight": "normal",
            "fontSize": "8px",
            "color": "#4d4d4f"
        },
        "symbolPadding": 3,
        "symbolRadius": 0,
        "symbolWidth": 7,
        "symbolHeight": 7
    },
    "credits": {
        "enabled": false
    },
    "xAxis": {
        "lineColor": "#a7a9ac",
        "tickColor": "#a7a9ac",
        "tickPosition": "inside",
        "tickLength": 4,
        "type": "category",
        "tickWidth": 0.5,
        "lineWidth": 0.5,
        "labels": {
            "enabled": true,
            "style": {
                "fontSize": "8px",
                "color": "#4d4d4f"
            }
        }
    },
    "exporting": {
        "scale": 1
    }
}""");

build();
