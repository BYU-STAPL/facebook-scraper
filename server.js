require('dotenv').config;

const express = require('express');
const cors = require('cors');
const path = require('path');
const { spawn } = require('child_process');

const PORT = process.env.PORT || 8080;

const app = express();

app.use(cors());
app.use(express.json());
app.use('/', express.static(path.join(__dirname, 'public')))

app.post('/api/login', async (req, res) => {
  console.log(req.body)
  const python = spawn("python3", ['scraper/main.py', req.body.username, req.body.password])
  python.stdout.on('data', (data)=>{
    console.log(data.toString())
  })

  python.stderr.on('data', (data)=>{
    console.log(`stderr: ${data}`)
  })

  python.on('exit', (PID)=>{
    console.log(`exited ${PID}`);
  })

  return res.json({ status: "success" });
});

app.listen(PORT, () => console.log(`server listing on ${PORT}`));