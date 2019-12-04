am4core.ready(function() {

  // Themes begin
  am4core.useTheme(am4themes_animated);
  // Themes end
  
  var chart = am4core.create("flowChart", am4charts.ChordDiagram);
  chart.hiddenState.properties.opacity = 0;

  chart.data = [];

  for(let i = 0; i < 10; i++) {
    chart.data.push(
      {from: flows[i][0], to: flows[i][1], value: flows[i][2]},
    );
  }
  
  chart.dataFields.fromName = "from";
  chart.dataFields.toName = "to";
  chart.dataFields.value = "value";
  
  // make nodes draggable
  var nodeTemplate = chart.nodes.template;
  nodeTemplate.readerTitle = "Click to show/hide or drag to rearrange";
  nodeTemplate.showSystemTooltip = true;
  nodeTemplate.cursorOverStyle = am4core.MouseCursorStyle.pointer
  
  }); // end am4core.ready()