import React from 'react'
export default class DataBar extends React.Component {


    render() {
        let marker = null;
        let key = "Please choose a marker...", pos = "";
        if (this.props.currMarker !== null && this.props.histData !== []) {
            marker = this.props.currMarker;
            key = "Filename: " +  marker.key;
            pos = "(Lat, Lng) = (" + marker.position.lat.toFixed(3) + ", " + marker.position.lng.toFixed(3) + ")";


            return (
                <div className="activated-databar">
                    <div className="device-info">
                        <h2 id="device-name">{key}</h2>
                        <h3 id="coordinates">{pos}</h3>
                    </div>
                    <div className="image">
                        <img id="image-instance"/>
                    </div>
                </div>
            );
        }
        else if (this.props.currMarker !== null && this.props.histData === []) {
            return (
                <div className="error-databar">
                    <h1>Can't retrieve data from server</h1>
                </div>
            );
        }
        return (
            <div className="default-databar">
                <h1>{key}</h1>
            </div>
        );
    }
}
