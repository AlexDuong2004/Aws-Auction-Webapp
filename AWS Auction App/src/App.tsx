// App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Users from './Users';
import Auctions from './Auctions';
import Bidding from './Bidding';
import './App.css';

const App: React.FC = () => {
  return (
    <Router>
      <nav className="navbar">
        <Link to="/users" className="nav-link">Users</Link>
        <Link to="/auctions" className="nav-link">Auctions</Link>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/users" element={<Users />} />
          <Route path="/auctions" element={<Auctions />} />
          <Route path="/bidding/:auctionId" element={<Bidding />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
