require('dotenv').config;

const express = require('express');
const cors = require('cors');
const path = require('path');

const PORT = process.env.PORT || 8080;

const app = express();

app.use(cors());
app.use(express.json());
app.use('/', express.static(path.join(__dirname, 'public')))

app.post('/api/login', async (req, res) => {
  console.log('it works!')
  return res.json({ status: "success" });
});

app.listen(PORT, () => console.log(`server listing on ${PORT}`));