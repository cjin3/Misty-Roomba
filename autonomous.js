misty.Debug("roomba mode");

let time = 10000;
let foundWall = false;

misty.AddPropertyTest("FrontTOFWall", "SensorPosition", "==", "Center", "string");
misty.AddPropertyTest("FrontTOFWall", "DistanceInMeters", "<=", 0.2, "double");
misty.RegisterEvent("FrontTOFWall", "TimeOfFlight", 250);

misty.AddPropertyTest("FrontTOFNoWall", "SensorPosition", "==", "Center", "string")
misty.AddPropertyTest("FrontTOFNoWall", "DistanceInMeters", ">", 0.2, "double");
misty.RegisterEvent("FrontTOFNoWall", "TimeOfFlight", 250);

autonomous();

function autonomous(){
    while (time > 0){
        misty.DriveTime(30, 0, 0.2);
        if (foundWall){
            turn();
        }
        time -= 1;
    }
}

function _FrontTOFWall(data){
    let frontTOF = data.PropertyTestResults[0].PropertyParent;
    misty.Debug("Found Wall!");
    misty.Debug(frontTOF.DistanceInMeters);
    foundWall = true;
}

function _FrontTOFNoWall(data){
    let frontTOF = data.PropertyTestResults[0].PropertyParent;
    misty.Debug("No More Wall!");
    misty.Debug(frontTOF.DistanceInMeters);
    foundWall = false;
}

function turn(){
    misty.DriveTime(0, 30, 0.2);
}