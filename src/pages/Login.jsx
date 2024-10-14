import React from 'react'
import { Button } from '../components/ui/button'
import { Input } from '../components/ui/input'
import bg_image from '../assets/login-bg.jpg'
import Title from '../components/Title'
import { Checkbox } from '../components/ui/checkbox'
import { useNavigate } from 'react-router-dom'
const Login = () => {
    const navigate = useNavigate();
    const handleLogin = () => {
        navigate('/home');
    }
  return (
    <div className="flex h-screen relative">
  {/* First section */}
  <div className="w-3/4 relative">
    <img
      src={bg_image}
      alt="Background"
      className="object-cover h-full w-full"
    />
    <div className="absolute inset-0 bg-gradient-to-r from-black opacity-50"></div> {/* Gradient overlay */}
  </div>
  {/* Second section */}
  <div className="relative bottom-[120px] w-1/4 flex items-center justify-start">
    <div className="bg-opacity-20 p-8 w-[80%] backdrop-blur-md shadow-lg">
      <div className="flex flex-col items-start gap-[36px]">
        <Title className="w-full font-bold text-2xl font-nito text-center">Login</Title>
        <Input type="email" placeholder="Email" className="bg-transparent w-full p-2 border-b border-gray-300 focus:outline-none" />
        <Input type="password" placeholder="Password" className="bg-transparent w-full p-2 border-b border-gray-300 focus:outline-none" />
        <div className="flex items-center gap-2">
          <Checkbox className="bg-white checked:bg-slate-400" />
          <label className="text-sm font-medium leading-none">
            Remember me
          </label>
        </div>
        <Button className="w-full bg-[#D1171A] hover:bg-[#D1171A50] text-white text-xs p-2 rounded-md" onClick={handleLogin}>
          Login
        </Button>
      </div>
    </div>
  </div>
</div>
  )
}

export default Login