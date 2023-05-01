import "./App.css";
import React from "react";
import bg from "./back2.mp4";
import { useForm } from "react-hook-form";
import { useState } from "react";

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm();
  const onSubmit = (data) => console.log(data);
  const [choice, setChoice] = useState(" ");
  const [choice1, setChoice1] = useState(" ");
  const [choice2, setChoice2] = useState(" ");
  const [choice3, setChoice3] = useState(" ");
  const [choice4, setChoice4] = useState(" ");
  const [choice5, setChoice5] = useState(" ");
  const [choice6 , setChoice6] = useState(" ");
  const [isShown, setIsShown] = useState(false);
  const [data , setData] = useState([{}]);
  const shoot = (event) => {
    setIsShown((current) => !current);
    event.preventDefault();
    fetch('/convert',{
      method : 'POST' ,
      headers : {
        'Content-Type' : 'application/x-www-form-urlencoded'
      },
      body : new URLSearchParams({
        'setChoice' : choice,
        'setChoice1' : choice1,
        'setChoice2' : choice2,
        'setChoice3' : choice3 ,
        'setChoice4' : choice4,
        'setChoice5' : choice5,
        'setChoice6' : choice6,
      })
    })
    .then(response => response.json())
    .then(data=>{setData(data)
    console.log(data)})
    .catch(error => console.error(error));
  };
  return (
    <section>
      <div className="App">
        <video src={bg} autoPlay loop muted />

        <div className="content">
          <div className="heading">
            <h1>Trip Estimation</h1>
            <span>Explore the world</span>
          </div>  
      
        
          <form id="form" onSubmit={handleSubmit(onSubmit)}>
            <div className="first">
              <div className="sc">
                 <h4>Source_City</h4>
              
              
                <select onChange={(e) => setChoice(e.target.value)}>
                  <option value=" "> Source City</option>
                  <option value="Chennai">Chennai</option>
                  <option value="Mumbai">Mumbai</option>
                  <option value="Delhi">Delhi</option>
                  <option value="Kolkata">Kolkata</option>
                  <option value="Hyderabad">Hyderabad</option>
                </select>

                
              
              </div>
              <div className="air">
                     <h4>Airlines</h4>
              
              
                <select onChange={(e) => setChoice2(e.target.value)}>
                  <option value=" "> Airlines</option>
                  <option value="AirAsia">Air Asia</option>
                  <option value="Air_India">Air India</option>
                  <option value="GO_FIRST">Go First</option>
                  <option value="SpiceJet">Spice Jet</option>
                  <option value="Indigo">Indigo</option>
                  <option value="Vistara">Vistara</option>

                </select>

                
              
              </div>
              <div className="dt">
                     <h4>Departure_time</h4>
              
              
                <select onChange={(e) => setChoice4(e.target.value)}>
                  <option value="Departure Time"> Departure Time</option>
                  <option value="Early_Morning">Early Morning</option>
                  <option value="Morning">Morning</option>
                  <option value="Afternoon">Afternoon</option>
                  <option value="Evening">Evening</option>
                  <option value="Night">Night</option>
                  <option value="Late_Night">Late Night</option>
                </select>

               
              
              </div>
            </div>
            <div className="second">
              <div className="dc">
                     <h4>Destination_City</h4>
              
              
                <select onChange={(b) => setChoice1(b.target.value)}>
                  <option value="Destination_City"> Destination City</option>
                  <option value="Chennai">Chennai</option>
                  <option value="Mumbai">Mumbai</option>
                  <option value="Delhi">Delhi</option>
                  <option value="Kolkata">Kolkata</option>
                  <option value="Hyderabad">Hyderabad</option>
                </select>

                
              
              </div>
             
              <div className="class">
                     <h4>Class</h4>
            
               
                <select onChange={(e) => setChoice3(e.target.value)}>
                  <option value=" "> Class</option>
                  <option value="Business">Business</option>
                  <option value="Economy">Economy</option>
                 
                </select>

                
              
              </div>
              
              <div className="nos">
                     <h4>Stops</h4>
              
              
                <select onChange={(e) => setChoice5(e.target.value)}>
                  <option value=" "> Stops</option>
                  <option value="0">0</option>
                  <option value="1">1</option>
                  <option value="2">2</option>
                 
                </select>
                
              </div>
              
            </div>
          <div className="third">
            <div className="d">
                     <h4>Date</h4>
              <input
               type="date"
               {...register("confirmpwd")}
               placeholder="dd-mm-yyyy"
               onChange = {(e) => setChoice6 (e.target.value)}
              />
              </div> 
            <button className="btn" onClick={shoot}>
              Estimate
            </button>
            {isShown && (
              <div className="side">
                <h4>{"Airfare-Rs."+data.prediction}</h4>
                <h4>Accomodation-Rs.3500</h4>
                <h4>Local Transport-Rs.5000</h4>
                <h4>Misc-Rs.2500</h4>
              </div>
            )}
          </div>
          </form>
        </div>
      </div>
    </section>
  );
}

