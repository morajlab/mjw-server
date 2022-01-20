import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    <div>
      <p>
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem quasi
        optio aut fugiat nemo ut ducimus recusandae, doloremque ipsa non
        reprehenderit unde cum. Deserunt illo rerum quasi nisi ab dolor.
      </p>
    </div>
  );
};

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
