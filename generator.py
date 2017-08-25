# ------------------------------------------------
# Template color schemes

clearwaterColors = """
        "#0A5EB2",
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

pathColors = """
        "#47BFAF",
        "#E94F3D",
        "#797D82",
        "#A9DBD3",
        "#F88771",
        "#797D82",
        "#C7C9C8",
        "#00B08F",
        "#282828",
        "#EFEFEF"
    """

# ------------------------------------------------
# Fonts

pathFont = '"Arial"'
clearwaterFont = '"Arial"'

# ------------------------------------------------
# Chart Font Color

pathChartColor = '"#4d4d4f"'
clearwaterChartColor = '"#4d4d4f"'

# ------------------------------------------------
# Chart Line Color

pathLineColor = '"#808080"'
clearwaterLineColor = '"#a7a9ac"'


def build():
    template = input('Which template? Type clearwater or path: ')

    if template == 'clearwater':
        colors = clearwaterColors
        font = clearwaterFont
        chartColor = clearwaterChartColor
        lineColor = clearwaterLineColor

    elif template == 'path':
        colors = pathColors
        font = pathFont
        chartColor = pathChartColor
        lineColor = pathLineColor

    chart = input('Chart type: ')

    if chart == 'column':
        width = input('Width: ')
        height = input('Height: ')
        dataLabels = input('Data labels enabled? Type true or false: ')
        legendEnabled = input('Legend enabled? Type true or false: ')
        print("""{
    "colors": [
        """ + colors + """], 
    
    "chart": {
        "type": """ +
              '"' + chart + '",' + """
        "width": """ + width + ',' + """
        "height": """ + height + ',' + """
        "style": {
            "fontfamily": """ + font + """
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
                "color": """ + chartColor + """,
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
        "lineColor": """ + lineColor + """,
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
                "color": """ + chartColor + """
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
            "color": """ + chartColor + """
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
        "lineColor": """ + lineColor + """,
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
                "color": """ + chartColor + """
            }
        }
    },
    "exporting": {
        "scale": 1
    }
}""")
    elif chart == "area":
        width = input('Width: ')
        height = input('Height: ')
        dataLabels = input('Data labels enabled? Type true or false: ')
        legendEnabled = input('Legend enabled? Type true or false: ')
        print("""{
                "colors": [
                    """ + colors + """], 

                "chart": {
                    "type": """ +
              '"' + chart + '",' + """
                    "width": """ + width + ',' + """
                    "height": """ + height + ',' + """
                    "style": {
                        "fontfamily": """ + font + """
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
                            "color": """ + chartColor + """,
                            "y": -2
                        }
                    },
                },
                "title": {
                    "text": null
                },
                "yAxis": {
                    "title": {
                        "text": null
                    },
                    "lineWidth": 0.5,
                    "lineColor": """ + lineColor + """,
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
                            "color": """ + chartColor + """
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
                        "color": """ + chartColor + """
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
                    "lineColor": """ + lineColor + """,
                    "tickColor": "#a7a9ac",
                    "tickPosition": "outside",
                    "tickLength": 4,
                    "type": "category",
                    "tickWidth": 0.5,
                    "lineWidth": 0.5,
                    "labels": {
                        "enabled": true,
                        "style": {
                            "fontSize": "8px",
                            "color": """ + chartColor + """
                        }
                    }
                },
                "exporting": {
                    "scale": 1
                }
            }""")
    elif chart == "pie":
        width = input('Width: ')
        height = input('Height: ')
        print("""
{
"colors": ["""
    + colors + """
], 
"chart": {
    "type": """ + '"' + chart + '",' + """
    "width": """ + width + ',' + """
    "height": """ + height + ',' + """
    "style": {
        "fontfamily": """ + font + """
        },
    "renderTo": "highchartContainer"
    },

 "plotOptions": {
    "pie": {
        "allowPointSelect": true,
        "cursor": true,
        "innerSize": "60%",
        "size": 135,
        "showInLegend": true,
        "dataLabels": {
            "enabled": false
        },
        "borderWidth": 0,
        "center": [
            null,
            null
        ]
    },
    "series": {}
},

"legend": {
    "itemWidth": 105,
    "align": "left",
    "enabled": false,
    "layout": "horizontal",
    "symbolRadius": 0,
    "y": -1,
    "floating": false,
    "itemStyle": {
        "fontSize": "9px",
        "width": 120,
        "fontWeight": "normal"
    }
},

"title": {
    "text": null
},

"yAxis": {
    "title": {
        "text": null,
        "style": {
            "fontSize": "8px"
        }
    },
    "labels": {
        "format": "{Series 1}"
    }
},

"xAxis": {
    "title": {
        "style": {
            "fontSize": "8px"
        }
    },
    "type": "category"
},

"credits": {
    "enabled": false
},

"exporting": {
    "scale": 1
}
}""")

build();
