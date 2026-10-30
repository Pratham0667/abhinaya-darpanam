export default function Register() {
  return (
    <div style={{ padding: '30px', fontFamily: 'Arial' }}>
      <h1>Create Your Account</h1>

      <form>
        <input type="text" placeholder="Full name" required />
        <br /><br />
        <input type="email" placeholder="Email address" required />
        <br /><br />
        <input type="password" placeholder="Password" required />
        <br /><br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
