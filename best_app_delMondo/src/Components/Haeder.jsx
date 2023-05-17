import React from "react";

const Header = () => {



    return(
        
        <header className="flex justify-between items-center py-4 px-6 bg-white border-b-2 border-primary">
        <div className="flex items-center p-3">
            TODO: inventare robe
        </div>

        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Reset
        </button>
        </header>
            
    )
}

export default Header
