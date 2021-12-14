import { useState } from "react";
import "./Content.css";
import Loading from "./types/Loading";
import Error from "./types/error";
import FITB from "./types/fitb";
import MCQ from "./types/mcq";
import fetchDataAPI from "./utilities/Data";
import Default from "./types/Default";

const Content = (props) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(false);
  const [fetchedContent, setFetchedContent] = useState(null);

  let content = <Default />;

  if (fetchedContent && props.showing === "FITB") {
    content = <FITB data={fetchedContent["context"]} />;
  }

  if (fetchedContent && props.showing === "MCQ") {
    content = <MCQ data={fetchedContent["domain"]} />;
  }

  if (error && !isLoading) content = <Error />;
  if (isLoading) content = <Loading />;

  const fetchData = (event) => {
    setIsLoading(true);
    setError(false);
    const context = document.getElementById("context").value;
    let limit = document.getElementById("limit").value;
    if (!(limit > 5 && limit < 25)) limit = 10;
    fetchDataAPI(context, limit, setError, setFetchedContent, setIsLoading);
  };

  const clear = () => {
    if (isLoading) return;
    document.getElementById("context").value = "";
  };

  return (
    <div className="container-fluid columns">
      <div className="row">
        <div className="col-md-5 column1">
          <div className="mb-0" id="context-out">
            <label className="form-label">Enter Context:</label>
            <textarea
              className="form-control mb-3 shadow-none"
              id="context"
              rows="13"></textarea>
            Enter number of FAQs to generate:{" "}
            <input
              type="number"
              id="limit"
              placeholder="10"
              min="5"
              max="25"></input>
          </div>
          <div className="container-fluid eval-buttons-cont">
            <button
              type="button"
              className="btn shadow-none navButtons m-0"
              onClick={fetchData}>
              Evaluate
            </button>
            <button
              type="button"
              className="btn shadow-none navButtons"
              onClick={clear}>
              Clear
            </button>
          </div>
        </div>
        <div className="col-md-7 column2">{content}</div>
      </div>
    </div>
  );
};
export default Content;
