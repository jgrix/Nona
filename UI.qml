import ThermoStat 1.0
import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls 1.4



TabView {
    property real fs: 15

   // Therm {
   //     id: myThermo
   // }


    Tab {
        title: "Therm"
        Rectangle { color: "Gray"

            Text {
                id:currentTempText
                font.pointSize: fs
                text: "Current Temp: "
                anchors.top: parent.top
                anchors.left: parent.left
            }



            Text {
                id:currentTempValue

                text: Therm.currentTemp
                font.pointSize: fs
                anchors.top: currentTempText.top
                anchors.left: currentTempText.right
            }

            Text {
                id: currentHumidityText
                font.pointSize: fs
                text: "Current Humidity: "
                anchors.top: currentTempText.bottom
                anchors.left: currentTempText.left

            }


            Text {
                id:currentHumidityValue
                text: "30"
                font.pointSize: fs
                anchors.top: currentHumidityText.top
                anchors.left: currentHumidityText.right
            }

            Text {
                id: targetTempatureText
                font.pointSize: fs
                text: "Target Tempature: "
                anchors.top: currentHumidityText.bottom
                anchors.left: currentHumidityText.left

            }


            Text {
                id:targetTempatureValue
                text: Therm.targetTemp
                font.pointSize: fs
                anchors.top: targetTempatureText.top
                anchors.left: targetTempatureText.right
            }

            Button {
                id: incraseTemp
                text: "Increase"
                anchors.bottom: parent.bottom
                anchors.left: parent.left
                height: 50
                width: 100
                onClicked: {
                    Therm.targetTemp++;
                }

            }

            Button {
                id: decreaseTemp
                text: "Decrease"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                height: 50
                width: 100

                onClicked: {
                    Therm.targetTemp--;
                }

            }
        }
    }

    Tab {
        title: "Weather"
        Rectangle { color: "Gray"

            Text {
                id: outSideTempText
                font.pointSize: fs
                text: "Outside Tempature: "
                anchors.top: parent.top
                anchors.left: parent.left

            }
            Text {
                id:outSideTempvalue
                text: "30"
                font.pointSize: fs
                anchors.top: outSideTempText.top
                anchors.left: outSideTempText.right
            }

            Text {
                id: relativeHumidityText
                font.pointSize: fs
                text: "Relative Humidity: "
                anchors.top: outSideTempText.bottom
                anchors.left: outSideTempText.left

            }
            Text {
                id:relativeHumidityValue
                text: "30"
                font.pointSize: fs
                anchors.top: relativeHumidityText.top
                anchors.left: relativeHumidityText.right
            }


            Text {
                id: windSpeedText
                font.pointSize: fs
                text: "Current Windspeed: "
                anchors.top: relativeHumidityText.bottom
                anchors.left: relativeHumidityText.left

            }
            Text {
                id: windSpeedValue
                text: myThermo.wind
                font.pointSize: fs
                anchors.top: windSpeedText.top
                anchors.left: windSpeedText.right
            }

            Text {
                id: highText
                font.pointSize: fs
                text: "High today: "
                anchors.top: windSpeedText.bottom
                anchors.left: windSpeedText.left

            }
            Text {
                id: highValue
                text: "30"
                font.pointSize: fs
                anchors.top: highText.top
                anchors.left: highText.right
            }

            Text {
                id: lowText
                font.pointSize: fs
                text: "Low today: "
                anchors.top: highText.bottom
                anchors.left: highText.left

            }
            Text {
                id: lowValue
                text: "30"
                font.pointSize: fs
                anchors.top: lowText.top
                anchors.left: lowText.right
            }




        }
    }
    Tab {
        title: "Costs"
        Rectangle { color: "green" }
    }
    Tab {
        title: "Mode"
        Rectangle { color: "Gray"

            property int currentIndex: 100



            Column {

                ExclusiveGroup { id: myGroup }
                RadioButton {
                    id: heatRadio
                    text: "Off"
                    checked: myThermo === 0


                    exclusiveGroup: myGroup
                    onClicked:{
                        myThermo.mode = 0
                    }

                }
                RadioButton {
                    id: offRadio
                    text: "Heat"
                    exclusiveGroup: myGroup
                    checked: myThermo === 1
                    onClicked:{
                        myThermo.mode = 1
                    }

                }
                RadioButton {
                    id: coolRadio
                    text: "Cool"
                    exclusiveGroup: myGroup
                    checked: myThermo === 2
                    onClicked:{
                        myThermo.mode = 2
                    }
                }
            }

        }
    }
}
