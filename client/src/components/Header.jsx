import logo from '../assets/logo.png'
import { NavLink } from 'react-router-dom';

function Header() {
  return (
    <div className='bg-beige p-3 pl-10 flex items-center justify-between'>
        <div className='flex items-center'>
          <img src={logo} alt="Friends Logo" className='h-12 -ml-3'/>
          <p className='ml-3 font-semibold text-2xl'>App</p>
        </div>
        <div className='flex gap-14 w-1/5'>
          <NavLink to="/">Classify Friend</NavLink>
          <NavLink to="/episodes">Episodes</NavLink>
        </div>
    </div>
  );
}

export default Header;