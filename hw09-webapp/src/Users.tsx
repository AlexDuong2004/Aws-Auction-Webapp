import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface User {
  userId: string;
  name: string;
  acctBalance: number;
}

const Users: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [form, setForm] = useState({
    userId: '',
    name: '',
    acctBalance: '',
  });

  const fetchUsers = async () => {
    const res = await axios.get(`${import.meta.env.VITE_REACT_APP_API_BASE}/user`);
    if (res.data.statusCode == 200) {
      setUsers(JSON.parse(res.data.body));
    } else {
      setUsers([]);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  };

  const handleCreate = async () => {
    const newUser = {
      userId: form.userId,
      name: form.name,
      acctBalance: parseFloat(form.acctBalance),
    };

    await axios.post(`${import.meta.env.VITE_REACT_APP_API_BASE}/user`, newUser, {
      headers: { 'Content-Type': 'application/json' },
    });

    // Reset form and refresh users
    setForm({ userId: '', name: '', acctBalance: '' });
    fetchUsers();
  };

  return (
    <div className="card">
      <h2>User List</h2>
      <table>
        <thead>
          <tr>
            <th>User ID</th>
            <th>Name</th>
            <th>Account Balance</th>
          </tr>
        </thead>
        <tbody>
          {users.length === 0 ? (
            <tr>
              <td colSpan={3}>No users found</td>
            </tr>
          ) : (
            users.map(user => (
              <tr key={user.userId}>
                <td>{user.userId}</td>
                <td>{user.name}</td>
                <td>${Number(user.acctBalance).toFixed(2)}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
      {/* <button onClick={fetchUsers}>Refresh</button> */}
      
      <h3>Create User</h3>
      <input
        name="userId"
        placeholder="User ID"
        value={form.userId}
        onChange={handleChange}
      />
      <input
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
      />
      <input
        name="acctBalance"
        placeholder="Balance"
        type="number"
        value={form.acctBalance}
        onChange={handleChange}
      />
      <button onClick={handleCreate}>Create</button>
    </div>
  );
};

export default Users;
