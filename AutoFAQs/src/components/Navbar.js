import "./Navbar.css";

const Navbar = (props) => {
  const fitb = () => {
    props.onChangeShowing("FITB");
  };
  const mcq = () => {
    props.onChangeShowing("MCQ");
  };

  return (
    <div id="navbar" className="container-fluid">
      <div className="name mb-0 h2">FAQ Generator</div>
      <div className="divider mt-3"></div>
      <div id="controls" className="container-fluid mt-1">
        <button
          type="button"
          className="btn shadow-none navButtons"
          onClick={fitb}>
          Context-based-Questions
        </button>
        <button
          type="button"
          className="btn shadow-none navButtons"
          onClick={mcq}>
          Domain-knowledge-Questions
        </button>
      </div>
    </div>
  );
};

export default Navbar;
