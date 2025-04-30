import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

interface Auction {
  auctionId: string;
  itemName: string;
  reserve: number;
  description: string;
  status: 'open' | 'closed';
  winningUserId?: string;
}

interface User {
  userId: string;
  name: string;
  acctBalance: number;
}

interface Bid {
  auctionId: string;
  bidAmt: number;
  date: string;
  userId: string;
}

const Bidding: React.FC = () => {
  const { auctionId } = useParams<{ auctionId: string }>();
  const [auction, setAuction] = useState<Auction | null>(null);
  const [users, setUsers] = useState<User[]>([]);
  const [bids, setBids] = useState<Bid[]>([]);  // Ensure bids is always an array
  const [selectedUserId, setSelectedUserId] = useState<string>('');
  const [bidAmt, setBidAmt] = useState<number>(0);
  const [bidsError, setBidsError] = useState<string | null>(null);  // Error state for bids

  const fetchAuction = async () => {
    try {
      const res = await axios.get(`${import.meta.env.VITE_REACT_APP_API_BASE}/auction/${auctionId}`);
      const data = JSON.parse(res.data.body)
      console.log("auctionId", auctionId)
      console.log("data", data)
      setAuction(data);
    } catch (error) {
      console.error("Error fetching auction:", error);
    }
  };

  const fetchUsers = async () => {
    try {
      const res = await axios.get(`${import.meta.env.VITE_REACT_APP_API_BASE}/user`);
      setUsers(JSON.parse(res.data.body));
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  const fetchBids = async () => {
    setBidsError(null); // Reset any previous errors
    try {
      const res = await axios.get(`${import.meta.env.VITE_REACT_APP_API_BASE}/bid?auctionId=${auctionId}`);
      const bidData = JSON.parse(res.data.body);
      
      if (Array.isArray(bidData)) {
        if (bidData.length === 0) {
          setBidsError('No bids placed yet.');
          setBids([]); // Make sure bids is an empty array if no bids are found
        } else {
          setBids(bidData); // Set bids if data is valid
        }
      } else {
        setBidsError('No bid data yet.');
        setBids([]); // Set bids to an empty array if the data is not an array
      }
    } catch (error) {
      console.error("Error fetching bids:", error);
      setBidsError('Error fetching bids for this auction.');
      setBids([]); // Ensure bids is an empty array in case of error
    }
  };

  useEffect(() => {
    fetchAuction();
    fetchUsers();
    fetchBids();
  }, [auctionId]);

  const placeBid = async () => {
    try {
      await axios.post(`${import.meta.env.VITE_REACT_APP_API_BASE}/bid`, {
        auctionId,
        bidAmt,
        date: new Date().toISOString(),
        userId: selectedUserId
      }, {
        headers: { 'Content-Type': 'application/json' }
      });
      fetchBids(); // Refresh bids after placing a bid
    } catch (error) {
      console.error("Error placing bid:", error);
    }
  };

  const closeAuction = async () => {
    try {
      await axios.put(`${import.meta.env.VITE_REACT_APP_API_BASE}/auction`, {
        auctionId,
        status: 'closed'
      }, {
        headers: { 'Content-Type': 'application/json' }
      });
      fetchAuction(); // Refresh auction status after closing
    } catch (error) {
      console.error("Error closing auction:", error);
    }
  };

  return (
    <div className="bidding-container">
      <div className="auction-details card">
        <h2>Auction Item: {auction?.itemName}</h2>
        <p>AuctionID: {auction?.auctionId}</p>
        {/* <p>Date: {auction?.date}</p> */}
        <p>Description: {auction?.description}</p>
        <p>Reserve: {auction?.reserve}</p>
        <p>Status: {auction?.status}</p>
        <p>Winning User: {auction?.winningUserId || 'N/A'}</p>
      </div>
      <div className="bidding-main">
        <div className="left card">
          <h3>Users</h3>
          {users.map(user => (
            <div key={user.userId}>
              <input
                type="radio"
                name="user"
                value={user.userId}
                checked={selectedUserId === user.userId}
                onChange={() => setSelectedUserId(user.userId)}
              />
              {user.userId}: {user.name} (Acct Balance: ${user.acctBalance})
            </div>
          ))}
          <input
            type="number"
            placeholder="Bid Amount"
            value={bidAmt}
            onChange={e => setBidAmt(Number(e.target.value))}
          />
          <button onClick={placeBid} disabled={auction?.status === 'closed'}>
            Place Bid
          </button>
        </div>
        <div className="right card">
          <h3>Bids</h3>
          <button onClick={fetchBids}>Refresh</button>
          {bidsError ? (
            <p>{bidsError}</p>  // Display error message if no bids or issue fetching
          ) : (
            <ul>
              {bids.length === 0 ? (
                <li>No bids placed yet.</li>  // Handle empty bids array
              ) : (
                bids.map((bid, idx) => (
                  <li key={idx}>
                    {bid.userId}: ${bid.bidAmt} ({new Date(bid.date).toLocaleString()})
                  </li>
                ))
              )}
            </ul>
          )}
        </div>
      </div>
      <button onClick={closeAuction} disabled={auction?.status === 'closed'}>
        Close Auction
      </button>
    </div>
  );
};

export default Bidding;
