export default function Practice() {
  return (
    <div style={{ padding: '30px', fontFamily: 'Arial' }}>
      <h1>Mudra Practice</h1>
      <p>Practice your Bharatanatyam hand gestures here.</p>

      <div
        style={{
          border: '2px dashed #1e3a8a',
          padding: '40px',
          maxWidth: '500px',
        }}
      >
        <p>Camera preview will appear here.</p>
        <button type="button">Start Practice</button>
      </div>
    </div>
  );
}
