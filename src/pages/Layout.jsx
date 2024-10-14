import React from 'react'
import { Outlet } from 'react-router-dom'

import Footer from './Footer'
import Header from './Header'

const Layout = () => {
  return (
    <div className='bg-[#191314] h-screen text-[#FEF2F3] font-nito'>
        <Header />
        <Outlet />
    </div>
  )
}

export default Layout