import axios from "axios";
import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [mode, setMode] = useState("compliance");

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await axios.post(
        `http://127.0.0.1:8000/analyze?mode=${mode}`,
        formData
      );

      setResult(res.data.analysis);
    } catch (err) {
      alert("Error analyzing file");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      {/* Sidebar */}
      <div style={styles.sidebar}>
        <h2 style={styles.logo}>ComplyAI</h2>
        <p style={styles.menuItem}>Dashboard</p>
        <p style={styles.menuItem}>Analyses</p>
        <p style={styles.menuItem}>Reports</p>
        <p style={styles.menuItem}>Settings</p>
      </div>

      {/* Main */}
      <div style={styles.main}>
        <h1 style={styles.title}>Security Analysis Dashboard</h1>

        {/* Upload Card */}
        <div style={styles.card}>
          <h3>Upload Document</h3>

          {/* Mode Selector */}
          <select
            value={mode}
            onChange={(e) => setMode(e.target.value)}
            style={styles.select}
          >
            <option value="compliance">Compliance</option>
            <option value="risk">Risk</option>
            <option value="tprm">TPRM</option>
            <option value="predictive">Predictive</option>
            <option value="threat">Threat Intel</option>
            <option value="zero-trust">Zero Trust</option>
          </select>

          {/* File Upload */}
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            style={styles.input}
          />

          {/* Button */}
          <button onClick={handleUpload} style={styles.button}>
            {loading ? "Analyzing..." : "Analyze"}
          </button>
        </div>

        {/* Result Card */}
        <div style={styles.card}>
          <h3>Analysis Result</h3>
          <pre style={styles.result}>
            {result || "Your analysis will appear here..."}
          </pre>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    height: "100vh",
    fontFamily: "Arial, sans-serif",
    backgroundColor: "#f5f6fa",
  },
  sidebar: {
    width: "220px",
    backgroundColor: "#1e293b",
    color: "#fff",
    padding: "20px",
  },
  logo: {
    marginBottom: "30px",
  },
  menuItem: {
    margin: "15px 0",
    cursor: "pointer",
    opacity: 0.85,
  },
  main: {
    flex: 1,
    padding: "30px",
  },
  title: {
    marginBottom: "20px",
  },
  card: {
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "10px",
    marginBottom: "20px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.05)",
  },
  select: {
    width: "100%",
    padding: "10px",
    marginTop: "10px",
    marginBottom: "10px",
    borderRadius: "5px",
    border: "1px solid #ccc",
  },
  input: {
    marginBottom: "10px",
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "#2563eb",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  result: {
    whiteSpace: "pre-wrap",
    fontSize: "14px",
    backgroundColor: "#f9fafb",
    padding: "10px",
    borderRadius: "5px",
  },
};

export default App;