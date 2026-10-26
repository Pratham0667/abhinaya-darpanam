import { useState } from 'react';

export default function Home() {
const [count, setCount] = useState(0);

return (
<div
style={{
minHeight: '100vh',
display: 'flex',
flexDirection: 'column',
alignItems: 'center',
justifyContent: 'center',
fontFamily: 'Inter, Arial, sans-serif',
backgroundColor: '#f8fafc',
color: '#1e3a8a',
}}
>
<h1>Abhinaya Darpanam</h1>

  <p>AI-Powered Bharatanatyam Mudra Recognition System</p>

  <hr style={{ width: '300px', margin: '24px 0' }} />

  <h2>React Counter Test</h2>

  <p style={{ fontSize: '48px', fontWeight: 'bold', margin: '16px' }}>
    {count}
  </p>

  <div style={{ display: 'flex', gap: '12px' }}>
    <button
      onClick={() => setCount(count - 1)}
      style={buttonStyle}
    >
      − Decrease
    </button>

    <button
      onClick={() => setCount(0)}
      style={buttonStyle}
    >
      Reset
    </button>

    <button
      onClick={() => setCount(count + 1)}
      style={buttonStyle}
    >
      + Increase
    </button>
  </div>

  <p style={{ marginTop: '24px', color: '#15803d' }}>
    Your React test page is ready!
  </p>
</div>

);
}

const buttonStyle = {
padding: '12px 18px',
border: 'none',
borderRadius: '8px',
backgroundColor: '#1e3a8a',
color: 'white',
cursor: 'pointer',
fontSize: '15px',
};