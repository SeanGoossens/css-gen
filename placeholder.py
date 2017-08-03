def code():
    print(("""
{
    "colors": [
        "#0A5EB2",
        "#00A2E0"
    ],
    "chart": {
        "type": "column",
        "width": 540.187,
        "height": 228.958,
        "style": {
            "fontFamily": "Arial"
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
                "enabled": true,
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
}
"""));

code();