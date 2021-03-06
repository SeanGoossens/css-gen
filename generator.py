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

jrColors = """
        "#0074AC",
        "#3FB6BE",
        "#6CC6E7",
        "#003660",
        "#1B7D7C",
        "#A0A0A0",
        "#797D82",
        "#C7C9C8",
        "#5FA7B6",
        "#3E5E85"
    """

# ------------------------------------------------
# Fonts

pathFont = '"Arial"'
clearwaterFont = '"Arial"'
jrFont = '"Arial"'


# ------------------------------------------------
# Font Size

clearwaterFontSize = '"8px"'
pathFontSize = '"8px"'
jrFontSize = '"9px"'


# ------------------------------------------------
# Chart Font Color

pathChartColor = '"#4d4d4f"'
clearwaterChartColor = '"#4d4d4f"'
jrChartColor = '"#4d4d4f"'

# ------------------------------------------------
# Chart Line Color

pathLineColor = '"#808080"'
clearwaterLineColor = '"#a7a9ac"'
jrLineColor = '"#808080"'


def build():
    template = input('Which template? clearwater, path, or jr: ')

    if template == 'clearwater':
        colors = clearwaterColors
        font = clearwaterFont
        fontSize = clearwaterFontSize
        chartColor = clearwaterChartColor
        lineColor = clearwaterLineColor

    elif template == 'path':
        colors = pathColors
        font = pathFont
        fontSize = pathFontSize
        chartColor = pathChartColor
        lineColor = pathLineColor

    elif template == 'jr':
        colors = jrColors
        font = jrFont
        fontSize = jrFontSize
        chartColor = jrChartColor
        lineColor = jrLineColor

    chart = input('Chart type: ')

    if chart == 'column':
        width = input('Width: ')
        height = input('Height: ')
        dataLabels = input('Data labels enabled? Type true or false: ')
        legendEnabled = input('Legend enabled? Type true or false: ')
        axisFormat = input('Y axis format? Hit enter for none or type one of the following ($,%, M): ')
        if axisFormat == '$':
            axisFormat = '"${value}"'
        elif axisFormat == '%':
            axisFormat = '"{value}%"'
        elif axisFormat == 'M':
            axisFormat = '"{value}M"'
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
                    "fontSize": """ + fontSize + """,
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
            "format": """ + axisFormat + """,
            "style": {
                "fontSize": """ + fontSize + """,
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
            "fontSize": """ + fontSize + """,
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
            "autoRotationLimit": 5,
            "style": {
                "fontSize": """ + fontSize + """,
                "textOverflow": "none",
                "lineHeight": 9,
                "color": """ + chartColor + """
            }
        }
    },
    "exporting": {
        "scale": 1
    }
}""")
    elif chart == "line":
        width = input('Width: ')
        height = input('Height: ')
        dataLabels = input('Data labels enabled? Type true or false: ')
        legendEnabled = input('Legend enabled? Type true or false: ')
        axisFormat = input('Y axis format? Hit enter for none or type one of the following ($,%, M): ')
        if axisFormat == '$':
            axisFormat = '"${value}"'
        elif axisFormat == '%':
            axisFormat = '"{value}%"'
        elif axisFormat == 'M':
            axisFormat = '"{value}M"'
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
                        "fontSize": """ + fontSize + """,
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
                "format": """ + axisFormat + """,
                "style": {
                    "fontSize": """ + fontSize + """,
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
                "fontSize": """ + fontSize + """,
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
                "autoRotationLimit": 5,
                "style": {
                    "fontSize": """ + fontSize + """,
                    "textOverflow": "none",
                    "lineHeight": 9,
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
        axisFormat = input('Y axis format? Hit enter for none or type one of the following ($,%, M): ')
        if axisFormat == '$':
            axisFormat = '"${value}"'
        elif axisFormat == '%':
            axisFormat = '"{value}%"'
        elif axisFormat == 'M':
            axisFormat = '"{value}M"'
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
                                "fontSize": """ + fontSize + """,
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
                        "format": """ + axisFormat + """,
                        "style": {
                            "fontSize": """ + fontSize + """,
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
                        "fontSize": """ + fontSize + """,
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
                            "fontSize": """ + fontSize + """,
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
        circle = input('Circle Size: ')
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
        "size": """ + circle + """,
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
        "fontSize": """ + fontSize + """,
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
            "fontSize": """ + fontSize + """
        }
    },
    "labels": {
        "format": "{Series 1}"
    }
},

"xAxis": {
    "title": {
        "style": {
            "fontSize": """ + fontSize + """
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
