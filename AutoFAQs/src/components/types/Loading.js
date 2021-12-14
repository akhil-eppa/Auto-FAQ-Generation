import { MDBIcon } from "mdbreact";
import "./Loading.css";

const Loading = () => {
  return (
    <div className="container-fluid loading">
      <MDBIcon icon="sync" spin size="3x" fixed />
    </div>
  );
};

export default Loading;
