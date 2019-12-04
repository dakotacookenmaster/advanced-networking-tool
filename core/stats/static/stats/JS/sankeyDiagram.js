am4core.ready(function() {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end
    
    var sankeyChart = am4core.create("sankeyChart", am4charts.SankeyDiagram);
    sankeyChart.hiddenState.properties.opacity = 0; // this creates initial fade-in
    
    sankeyChart.data = [];

    for(let i = 0; i < 4; i++) {
        console.log(String(flows[i][0]), String(flows[i][1]), Number(flows[i][2]));
        sankeyChart.data.push(
          {from: flows[i][0], to: flows[i][1], value: flows[i][2]},
        );
    }
    console.log(sankeyChart.data);
    
    let hoverState = sankeyChart.links.template.states.create("hover");
    hoverState.properties.fillOpacity = 0.6;
    
    sankeyChart.dataFields.fromName = "from";
    sankeyChart.dataFields.toName = "to";
    sankeyChart.dataFields.value = "value";
    
    // for right-most label to fit
    sankeyChart.paddingRight = 30;
    
    // make nodes draggable
    var nodeTemplate = sankeyChart.nodes.template;
    nodeTemplate.inert = true;
    nodeTemplate.readerTitle = "Drag me!";
    nodeTemplate.showSystemTooltip = true;
    nodeTemplate.width = 20;
    
    // make nodes draggable
    var nodeTemplate = sankeyChart.nodes.template;
    nodeTemplate.readerTitle = "Click to show/hide or drag to rearrange";
    nodeTemplate.showSystemTooltip = true;
    nodeTemplate.cursorOverStyle = am4core.MouseCursorStyle.pointer
    
    }); // end am4core.ready()