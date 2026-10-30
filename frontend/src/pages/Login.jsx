export default function Login() {
  return (
    <div style={{ padding: '30px', fontFamily: 'Arial' }}>
      <h1>Login</h1>
      <p>Welcome back to Abhinaya Darpanam!</p>

      <form>
        <input type="email" placeholder="Email address" required />
        <br /><br />
        <input type="password" placeholder="Password" required />
        <br /><br />
        <button type="submit">Login</button>
      </form>

      <p>Login page is working!</p>
    </div>
  );
}