import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
// import './Auctions.css'; // Import the CSS file

interface Auction {
  auctionId: string;
  itemName: string;
  reserve: number;
  description: string;
  status: 'open' | 'closed';
  winningUserId?: string;
}

const Auctions: React.FC = () => {
  const [auctions, setAuctions] = useState<Auction[]>([]);
  const [selectedId, setSelectedId] = useState<string>('');
  const [form, setForm] = useState<Partial<Auction>>({});
  const navigate = useNavigate();

  const fetchAuctions = async () => {
    const res = await axios.get(`${import.meta.env.VITE_REACT_APP_API_BASE}/auction`);
    if (res.data.statusCode == 200) {
      setAuctions(JSON.parse(res.data.body));
    } else {
      setAuctions([]);
    }
  };

  useEffect(() => {
    fetchAuctions();
  }, []);

  // const toggleAuctionStatus = async () => {
  //   const selected = auctions.find(a => a.auctionId === selectedId);
  //   if (!selected) return;
  //   const newStatus = selected.status === 'open' ? 'closed' : 'open';
  //   await axios.put(`${import.meta.env.VITE_REACT_APP_API_BASE}/auction`, {
  //     auctionId: selected.auctionId,
  //     status: newStatus
  //   }, {
  //     headers: { 'Content-Type': 'application/json' }
  //   });
  //   fetchAuctions();
  // };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm(prev => ({
      ...prev,
      [name]: name === 'reserve' ? Number(value) : value
    }));
  };

  const createAuction = async () => {
    const auctionData = {
      ...form,
      status: 'open'
    };

    await axios.post(`${import.meta.env.VITE_REACT_APP_API_BASE}/auction`, auctionData, {
      headers: { 'Content-Type': 'application/json' }
    });
    fetchAuctions();
    // Clear form
    setForm({});
  };

  const isAuctionListEmpty = auctions.length === 0;
  const isGoToBiddingDisabled = isAuctionListEmpty || !selectedId;
  // const isToggleAuctionStatusDisabled = isAuctionListEmpty || !selectedId;

  return (
    <div className="card">
      <h2>Auctions</h2>

      {/* Auctions Table */}
      <table className="auction-table" >
        <thead>
          <tr>
            <th>Auction ID</th>
            <th>Item Name</th>
            <th>Reserve</th>
            <th>Description</th>
            <th>Status</th>
            <th>Winning User ID</th>
          </tr>
        </thead>
        <tbody>
          {auctions.map(a => (
            <tr key={a.auctionId}>
              <td>
                <input
                  type="radio"
                  name="selectedAuction"
                  value={a.auctionId}
                  checked={selectedId === a.auctionId}
                  onChange={() => setSelectedId(a.auctionId)}
                />
                {a.auctionId}
              </td>
              <td>{a.itemName}</td>
              <td>{a.reserve}</td>
              <td>{a.description}</td>
              <td>{a.status}</td>
              <td>{a.winningUserId ?? 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Buttons */}
      <button 
        onClick={() => navigate(`/bidding/${selectedId}`)} 
        disabled={isGoToBiddingDisabled}
      >
        Go to Bidding
      </button>
      {/* <button 
        onClick={toggleAuctionStatus} 
        disabled={isToggleAuctionStatusDisabled}
      >
        {auctions.find(a => a.auctionId === selectedId)?.status === 'open' ? 'Close Auction' : 'Open Auction'}
      </button> */}

      {/* Create Auction Form */}
      <h3>Create Auction</h3>
      <input name="auctionId" placeholder="Auction ID" onChange={handleChange} />
      <input name="itemName" placeholder="Item Name" onChange={handleChange} />
      <input name="reserve" placeholder="Reserve" type="number" onChange={handleChange} />
      <input name="description" placeholder="Description" onChange={handleChange} />

      <button onClick={createAuction}>Create Auction</button>
    </div>
  );
};

export default Auctions;
