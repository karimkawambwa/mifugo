import App from "./components/App";

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;