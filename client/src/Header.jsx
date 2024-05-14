// import React from 'react';
import logo from './assets/logo.png'

function Header() {
  return (
    <div className='bg-beige p-3 flex justify-center items-center'>
        <img src={logo} alt="Friends Logo" className='h-12 -ml-3'/>
        <p className='ml-3 font-semibold text-2xl'>Detection App</p>
    </div>
  );
}

export default Header;
