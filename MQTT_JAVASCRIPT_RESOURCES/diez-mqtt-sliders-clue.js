var broker = 'wss://mqtt.eclipseprojects.io:443/mqtt'; //intializing the variable broker
var client = mqtt.connect(broker); //initializing the variable client 
var status_header = document.getElementById('status-header') //intializing the status_header 

//connection of the broker
client.on('connect', function() {
    status_header.innerHTML = 'Connected to ' + broker; //this line displays the broker if it is connected successfully.
    console.log('Connected to ' + broker) //console the broker to check if it is connected succesfully
})


var sliders = document.getElementsByClassName("slider"); //Initializing the variable sliders

//this code has the variable that handles two events
const events = {
    "mouseup": function(event) { //creating the function that having the parameter event which is mouseup event
        console.log(event.target.name, event.target.value); //console log to check
        client.publish(`clueSlider/${event.target.name}`, event.target.value); //publish now the target topic or the name and its target value
    },
    "input": function(event) { //input the element
        document.getElementById(event.target.name).innerHTML = event.target.value;
    }
}

//loop all the sliders   
for (let slider of sliders) {
    for (let key in events) { //loop the events variable to loop through all the events to get the specific event
        slider.addEventListener(key, events[key]); //slider.addEventListener(key, events[key])
    }
}