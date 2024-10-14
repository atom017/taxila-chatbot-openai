import React from 'react'
import { Link, NavLink } from 'react-router-dom'
import logo_icon from '../assets/icons/logo.svg'
import Title from '../components/Title'
import { Button } from '../components/ui/button'
import {
    Avatar,
    AvatarFallback,
    AvatarImage,
  } from "./../components/ui/avatar"
import { useLocation } from 'react-router-dom'
const Header = () => {
    let {pathname} = useLocation();
    console.log(location)
    return (
        <nav className="flex p-5 w-full justify-between z-10 absolute">
            <Title className="font-bold text-[32px]">Taxila</Title>  
            
                {
                    pathname !== '/login' ? <Button>Logout</Button>: 
                    <Avatar className='rounded-none'>
                        <AvatarImage src={logo_icon} alt="@shadcn" />
                        <AvatarFallback>Taxila Logo</AvatarFallback>
                    </Avatar>
                }
        </nav>
    )
}

export default Header