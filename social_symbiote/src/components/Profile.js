import { useState, useEffect } from 'react';
import modules from './Profile.module.css'
import Card from 'react-bootstrap/Card';
function Profile(props) {
  const [clicked, setclicked] = useState(false);
  return (
    <Card className={modules.card}>
      <Card.Body>
        <div style={{ maxWidth: "200px", margin: "1rem" }}>
          <img src={props.image} style={{ width: '50%', height: '50%', alignItems: 'center', justifyContent: 'center' }}></img>
          <h1>{props.name}</h1>
          <p>{props.text}</p>
        </div>
      </Card.Body>
    </Card>

  )
}
export default Profile; 