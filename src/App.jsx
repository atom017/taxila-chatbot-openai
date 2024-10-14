import viteLogo from '/vite.svg'
import { useState } from 'react'
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider, Routes } from 'react-router-dom'

import reactLogo from './assets/react.svg'
import Layout from './pages/Layout'
import Login from './pages/Login'
import PrivateRoute from './pages/PrivateRoute'
import Home from './pages/Home'
import './App.css'

const router = createBrowserRouter(createRoutesFromElements(
  <Route>
    <Route element={<Layout />} >
    <Route path="/login" element={<Login />} />
    <Route path="/home" element={<PrivateRoute><Home /></PrivateRoute>} />
    </Route>
  </Route>
))
function App({children}) {

  return (
    <RouterProvider router={router}>
      {children}
    </RouterProvider>
  )
}

export default App
