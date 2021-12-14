import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Content from "./components/Content";
import Navbar from "./components/Navbar";

function App() {
  const [showing, setShowing] = useState("FITB");
  const [answers, setAnswers] = useState(false);
  const changeShowing = (type) => {
    setShowing(type);
  };
  const changeAnswers = () => {
    setAnswers((prev) => !prev);
  };
  return (
    <div className="App">
      <Navbar onChangeShowing={changeShowing} onChangeAnswers={changeAnswers} />
      <Content showing={showing} answers={answers} />
    </div>
  );
}

export default App;
