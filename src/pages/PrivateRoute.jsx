import React from 'react'
import { Navigate } from 'react-router-dom';
const PrivateRoute = ({children}) => {
    const isAuthenticated = Math.random() >= 0.5; // Replace this with your authentication logic
    return isAuthenticated ? children : <Navigate to="/login" />;
}

export default PrivateRoute