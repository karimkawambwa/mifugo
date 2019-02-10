import React from "react";
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => (
  <DataProvider endpoint="api/ngombe/" render={data => <Table data={data} />} />
);

export default App
