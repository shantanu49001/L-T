import React from 'react';
import ReactDOM from 'react-dom/client';

import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();

/*
{
  supplier_id: "";
  customer_id: "";
  prev_loc: []//prev delivery centre params
  current_loc: []//current delivery centre params
}*/