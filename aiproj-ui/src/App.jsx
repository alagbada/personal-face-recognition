import { useEffect, useState } from 'react'
import Webcam from "react-webcam";
import { MoonLoader } from 'react-spinners';
import {predictImage} from './logic/apilogic';
import side from './assets/side.jpg'
import './App.css'

function App() {
  const [imgsrc, setImgSrc] = useState(null)
  const [isConnecting, setIsConnecting] = useState(false)
  const [isCapture, setIsCapture] = useState(false)
  const [match, setMatch] = useState(-1)
  const videoConstraints = {
    width: 200,
    height: 200,
    facingMode: "user"
  };

  useEffect(() => {
    (async() => {
      const resp = parseFloat(await predictImage(imgsrc)) * 100
      setMatch(resp)
      setIsCapture(false)
      setIsConnecting(false)
    })()
    
  }, [imgsrc]);

  return (
    <div className='mainsection'>
      <div className='rightsection'>
        <h2>Personal Face Detection App</h2>
        <div style={{'padding': '2%'}}>
          <p>To login to the app, you are required to scan your face by clicking on the button below
             so we can verify that it is you. 
            In seconds, if you are the real user that is configured to access this resources, 
            you will be granted access classified information. 
            A pop-up will appear requesting for webcam access, please allow.</p>
        </div>
        <div className='loader'>
          <MoonLoader 
            color={'#ffffff'}
            loading={isConnecting}
          />
        </div>
        <div className='notification'>
          {match !== -1 ? (<div>The Face Match is {match}%</div>) : (<></>)}
          {
            match >= 99 
            ? 
              (<div className='successNotification'>Hooray! Your face recognition is successful</div>) 
            : 
              (match !== -1) 
              ? 
              (<div className='failedNotification'>Face recognition failed. Please try again</div>)
              : (<></>)
            }
          {
            !isCapture ? (<button onClick={() => setIsCapture(true)}>Scan Your Face</button>) 
            : 
            (
              <Webcam 
                audio={false}
                height={200}
                width={200}
                screenshotFormat='image/jpeg'
                videoConstraints={videoConstraints}
                screenshotQuality={0.97}
              >
                {({ getScreenshot }) => (
                  <div>
                    <button
                    onClick={() => {
                      setIsConnecting(true)
                      setImgSrc(getScreenshot())
                    }}
                    >
                      Capture photo
                    </button>
                  </div>
                )}
              </Webcam>
            )
          }
        </div>
      </div>
      <div className='leftsection'>
        <img 
          src={side} 
          width={'100%'}
          alt='img for face scan'
          />
      </div>
    </div>
  )
}

export default App
