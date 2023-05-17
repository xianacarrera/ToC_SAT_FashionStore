

import React, { useEffect, } from "react";
import Header from "./Components/Haeder";
import Home
from "./Components/Home";
import { BrowserRouter, Routes, Route } from 'react-router-dom'


function App() {
  useEffect(() => {
    if(window.location.href !== "http://localhost:3000/home"){
        console.log(window.location.href)
        window.location.href = "http://localhost:3000/home";
    }
}, [])

  return (
    <div className={`flex h-screen bg-gray-200 overflow-hidden `}>
    <div className="flex-1 flex flex-col overflow-hidden">
      <Header />
      <BrowserRouter basename='/'>
        <Routes>
          <Route path='/home' element={<Home />} />
        </Routes>
    </BrowserRouter>
    </div>
  </div>
  
  );
}

export default App;
