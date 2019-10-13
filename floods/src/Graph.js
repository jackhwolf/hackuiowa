import './graphstyle.scss';
import React from 'react';
import {
  XYPlot,
  XAxis,
  YAxis,
  VerticalGridLines,
  HorizontalGridLines,
  VerticalBarSeries,
  VerticalBarSeriesCanvas,
  LabelSeries
} from 'react-vis';


export default class Graph extends React.Component {

  constructor(props) {
    super(props)
    this.state = {};
    var hasChanged = 0;
  }

  render() {
    const {useCanvas} = this.state;
    const BarSeries = useCanvas ? VerticalBarSeriesCanvas : VerticalBarSeries;
    if (this.hasChanged === 0) {
      this.props.changeState()
      this.state = -1
    }
    return (
      <div>
        <XYPlot xType="ordinal" width={500} height={500} xDistance={100}>
          <VerticalGridLines />
          <HorizontalGridLines />
          <XAxis />
          <YAxis />
          <BarSeries className="vertical-bar-series-example" data={this.props.data} />
        </XYPlot>
      </div>
    );
  } 
}