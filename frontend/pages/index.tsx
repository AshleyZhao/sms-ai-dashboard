import { useState } from 'react'
import axios from 'axios'

export default function Home() {
  const [productName, setProductName] = useState('')
  const [tone, setTone] = useState('friendly')
  const [message, setMessage] = useState('')

  const generateSMS = async () => {
    const res = await axios.post('http://localhost:8000/api/generate-sms', {
      product_name: productName,
      tone,
    })
    setMessage(res.data.message)
  }

  return (
    <main>
      <h1>AI SMS Generator</h1>
      <input value={productName} onChange={e => setProductName(e.target.value)} placeholder="Product name" />
      <select value={tone} onChange={e => setTone(e.target.value)}>
        <option value="friendly">Friendly</option>
        <option value="urgent">Urgent</option>
        <option value="funny">Funny</option>
        <option value="professional">Professional</option>
      </select>
      <button onClick={generateSMS}>Generate SMS</button>
      <p>{message}</p>
    </main>
  )
}