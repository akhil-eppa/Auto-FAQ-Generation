import "./fitb.css";

const FITB = (props) => {
  const questions = [];
  const answers = [];
  props.data.forEach((item) => {
    let ques = item.question;
    let ans = item.answer;
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
export default FITB;
