// Print a message to indicate the skill has started
misty.Debug("starting skill helloworld_timeofflight");

var REGTIME = 100;

// Issue commands to change LED and start driving
misty.ChangeLED(0, 255, 0); // green, GO!
misty.DriveTime(7, 0, 1000000);

// Register for TimeOfFlight data and add property tests
misty.AddPropertyTest("FrontTOF", "SensorPosition", "==", "Center", "string");
misty.AddPropertyTest("FrontTOF", "DistanceInMeters", "<=", 0.2, "double");
misty.RegisterEvent("FrontTOF", "TimeOfFlight", REGTIME);

// FrontTOF callback function
function _FrontTOF(data) {
    // Get property test results
    let frontTOF = data.PropertyTestResults[0].PropertyParent;

    // Print distance object was detected and sensor
    misty.Debug(frontTOF.DistanceInMeters);
    misty.Debug(frontTOF.SensorPosition);
    // Issue commands to change LED and stop driving
    misty.ChangeLED(0, 0, 255);
    misty.DriveTime(0, -30, 1000000);
    misty.Pause(2900);

    misty.AddPropertyTest("FrontNoTOF", "SensorPosition", "==", "Center", "string");
    misty.AddPropertyTest("FrontNoTOF", "DistanceInMeters", ">", 0.2, "double");
    misty.RegisterEvent("FrontNoTOF", "TimeOfFlight", REGTIME);
    misty.Debug("ending skill helloworld_timeofflight ");
}

function _FrontNoTOF(data){
    misty.ChangeLED(0,255,0);
    misty.DriveTime(3, 0, 100000);

    misty.AddPropertyTest("FrontTOF", "SensorPosition", "==", "Center", "string");
    misty.AddPropertyTest("FrontTOF", "DistanceInMeters", "<=", 0.2, "double");
    misty.RegisterEvent("FrontTOF", "TimeOfFlight", REGTIME);
}