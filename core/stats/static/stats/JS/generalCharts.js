/**
 * --------------------------------------------------------
 * This demo was created using amCharts V4 preview release.
 * 
 * V4 is the latest installement in amCharts data viz
 * library family, to be released in the first half of
 * 2018.
 *
 * For more information and documentation visit:
 * https://www.amcharts.com/docs/v4/
 * --------------------------------------------------------
 */

am4core.useTheme(am4themes_animated);

let chart = am4core.create("generalCharts", am4charts.XYChart);

chart.data = [{
  "country": "One",
  "value": 3025
}, {
  "country": "Two",
  "value": 1882
}, {
  "country": "Three",
  "value": 1809
}, {
  "country": "Four",
  "value": 1322
}, {
  "country": "Five",
  "value": 1122
}, {
  "country": "Six",
  "value": -1114
}, {
  "country": "Seven",
  "value": -984
}, {
  "country": "Eight",
  "value": 711
}, {
  "country": "Nine",
  "value": 665
}, {
  "country": "Ten",
  "value": -580
}, {
  "country": "Eleven",
  "value": 443
}, {
  "country": "Twelve",
  "value": 441
}];


let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.renderer.grid.template.location = 0;
categoryAxis.dataFields.category = "country";
categoryAxis.renderer.minGridDistance = 40;

let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

let series = chart.series.push(new am4charts.CurvedColumnSeries());
series.dataFields.categoryX = "country";
series.dataFields.valueY = "value";
series.tooltipText = "{valueY.value}"
series.columns.template.strokeOpacity = 0;

chart.cursor = new am4charts.XYCursor();

// Add distinctive colors for each column using adapter
series.columns.template.adapter.add("fill", (fill, target) => {
  return chart.colors.getIndex(target.dataItem.index);
});