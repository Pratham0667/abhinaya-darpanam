
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "./App.css";

function Home() {
  return (
    <div>
      <nav className="navbar">
        <h2>Abhinaya Darpanam</h2>
        <div className="nav-links">
          <a href="#about">About</a>
          <Link to="/login">Login</Link>
          <Link to="/register" className="register-btn">
            Register
          </Link>
        </div>
      </nav>

      <section className="hero">
        <p className="tagline">WHERE TRADITION MEETS TECHNOLOGY</p>
        <h1>Discover the Art of Bharatanatyam</h1>
        <p>
          Learn mudras, practise your gestures, and improve your
          performance with AI-powered guidance.
        </p>
        <Link to="/login" className="primary-btn">
          Start Practising →
        </Link>
      </section>

      <section id="about" className="about">
        <h2>Your Dance Journey, Guided by AI</h2>
        <p>
          Abhinaya Darpanam helps learners recognise Bharatanatyam
          mudras and receive feedback to improve hand gestures.
        </p>
      </section>
    </div>
  );
}

function Login() {
  return (
    <div className="simple-page">
      <h1>Login</h1>
      <p>Welcome back to Abhinaya Darpanam!</p>
      <Link to="/">← Back to Home</Link>
    </div>
  );
}

function Register() {
  return (
    <div className="simple-page">
      <h1>Create Your Account</h1>
      <p>Start your Bharatanatyam learning journey.</p>
      <Link to="/">← Back to Home</Link>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}
