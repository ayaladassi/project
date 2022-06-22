import * as React from 'react';
import { useLocation } from 'react-router-dom';


export default function Winner() {
    const location = useLocation()
   
    return(
        <div>
<p>

</p>

<div></div>
        
        <h1>The {location.state} Group - wins</h1>
        </div>
    )
};