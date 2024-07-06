import './App.css'
import Timer from './components/Timer'
import FancyTimer from './components/FancyTimer'
import { useState } from 'react'

function App() {
  const [showTimer, setShowTimer] = useState(true)

  return (
    <>
      <Timer />
      
      {showTimer && (
        <>
          <FancyTimer />
          <button onClick={() => setShowTimer(false)}>TunOff</button>
        </>
      )}
    </>
  )
}

export default App
