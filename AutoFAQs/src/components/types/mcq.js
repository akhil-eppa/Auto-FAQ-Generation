import "./mcq.css";

const MCQ = (props) => {
  // console.log(props.data);
  const questions = [];
  const answers = [];
  props.data.forEach((item) => {
    let ques = item.ques;
    let ans = item.ans;
    questions.push(ques);
    answers.push(ans);
  });
  return (
    <div className="container-fluid">
      <div className="questions">
        {questions.map((op, i) => (
          <div className="ques" key={i}>
            {(i + 1).toString() + " ) "}
            {op}
            <div className="ans" key={i}>
              {"Ans: "}
              {answers[i]}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MCQ;
